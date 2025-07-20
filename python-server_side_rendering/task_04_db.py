#!/usr/bin/python3
from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

# Read from JSON
def read_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except Exception:
        return []

# Read from CSV
def read_csv(file_path):
    try:
        with open(file_path, newline='') as f:
            reader = csv.DictReader(f)
            return [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                for row in reader
            ]
    except Exception:
        return []

# Read from SQLite
def read_sqlite(db_path, id=None):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
            rows = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()

        conn.close()

        return [dict(row) for row in rows]
    except Exception as e:
        return f"Database error: {e}"

@app.route('/products')
def show_products():
    source = request.args.get("source")
    id_param = request.args.get("id")
    products = []
    error = None

    # Validate source
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source", products=[])

    # Try converting ID
    product_id = None
    if id_param:
        try:
            product_id = int(id_param)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format", products=[])

    # Load data based on source
    if source == "json":
        products = read_json("products.json")
    elif source == "csv":
        products = read_csv("products.csv")
    elif source == "sql":
        data = read_sqlite("products.db", product_id)
        if isinstance(data, str):  # It's an error string
            return render_template("product_display.html", error=data, products=[])
        products = data

    # Filter manually for json/csv
    if source in ["json", "csv"] and product_id is not None:
        products = [p for p in products if p.get("id") == product_id]

    if not products:
        error = "Product not found"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
