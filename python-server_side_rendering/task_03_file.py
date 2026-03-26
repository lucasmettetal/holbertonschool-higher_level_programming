"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""

from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """Display products from JSON or CSV depending on query parameter."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    try:
        if source == "json":
            products_list = read_products_from_json()
        else:
            products_list = read_products_from_csv()
    except (FileNotFoundError, json.JSONDecodeError, KeyError, ValueError):
        return render_template("product_display.html", error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found")

        filtered_products = [
            product for product in products_list
            if product.get("id") == product_id
        ]

        if not filtered_products:
            return render_template(
                "product_display.html",
                error="Product not found")

        return render_template(
            "product_display.html",
            products=filtered_products)

    return render_template("product_display.html", products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
