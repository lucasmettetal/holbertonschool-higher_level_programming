"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_products_from_json():
    """Read products from JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_products_from_csv():
    """Read products from CSV file."""
    products = []
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


def read_products_from_sql():
    """Read products from SQLite database."""
    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    try:
        if source == "json":
            products_list = read_products_from_json()
        elif source == "csv":
            products_list = read_products_from_csv()
        else:
            products_list = read_products_from_sql()
    except Exception:
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        filtered_products = [
            product for product in products_list
            if int(product["id"]) == product_id
        ]

        if not filtered_products:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        return render_template(
            "product_display.html",
            products=filtered_products
        )

    return render_template("product_display.html", products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
