#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path) as f:
            return json.load(f)
    except Exception:
        return []

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

@app.route('/products')
def show_products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source", products=[])

    # Load data
    if source == "json":
        products = read_json("products.json")
    else:
        products = read_csv("products.csv")

    # If an id is provided, try to filter it
    if id_param:
        try:
            product_id = int(id_param)
            products = [p for p in products if int(p["id"]) == product_id]
            if not products:
                return render_template("product_display.html", error="Product not found", products=[])
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format", products=[])

    return render_template("product_display.html", products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
