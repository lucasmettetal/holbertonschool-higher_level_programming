"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask

Demonstrates fetching and displaying data from SQLite database
with error handling.
"""

import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE = 'products.db'


def create_database():
    """Create database and products table if they don't exist."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    ''')

    # Check if table is empty, then insert sample data
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (name, price, category)
            VALUES (?, ?, ?)
        ''', ('Laptop', 799.99, 'Electronics'))
        cursor.execute('''
            INSERT INTO Products (name, price, category)
            VALUES (?, ?, ?)
        ''', ('Coffee Mug', 15.99, 'Home Goods'))

    conn.commit()
    conn.close()


def get_products_from_sql():
    """Fetch products from SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, price, category FROM Products')
        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.DatabaseError:
        return None


def get_products_from_json():
    """Return products in JSON format (from memory)."""
    return [
        {
            'id': 1,
            'name': 'Laptop',
            'price': 799.99,
            'category': 'Electronics'
        },
        {
            'id': 2,
            'name': 'Coffee Mug',
            'price': 15.99,
            'category': 'Home Goods'
        }
    ]


def get_products_from_csv():
    """Return products in CSV format (from memory)."""
    products = [
        {
            'id': 1,
            'name': 'Laptop',
            'price': 799.99,
            'category': 'Electronics'
        },
        {
            'id': 2,
            'name': 'Coffee Mug',
            'price': 15.99,
            'category': 'Home Goods'
        }
    ]
    return products


@app.route('/')
def index():
    """Home page."""
    return render_template('product_display.html', products=[], error=None)


@app.route('/products')
def products():
    """Display products based on source parameter."""
    source = request.args.get('source', 'sql').lower()

    error = None
    products_data = []

    if source == 'sql':
        products_data = get_products_from_sql()
        if products_data is None:
            error = (
                'Database error: Unable to fetch products '
                'from SQLite database'
            )
            products_data = []
    elif source == 'json':
        products_data = get_products_from_json()
    elif source == 'csv':
        products_data = get_products_from_csv()
    else:
        error = (
            f'Wrong source: {source}. Valid sources are: '
            'json, csv, sql'
        )
        products_data = []

    return render_template(
        'product_display.html',
        products=products_data,
        error=error
    )


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
