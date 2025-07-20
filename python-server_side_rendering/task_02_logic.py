#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        # Load items from the JSON file
        with open('items.json') as f:
            data = json.load(f)
            item_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []

    return render_template("items.html", items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
