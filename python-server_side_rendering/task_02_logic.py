#!/usr/bin/env python3
"""
Flask application with dynamic content using Jinja loops and conditions
"""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with dynamic content from JSON"""
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file = os.path.join(script_dir, 'items.json')

        # Read the JSON file
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Extract items list
        items_list = data.get('items', [])

        # Pass items to template
        return render_template('items.html', items=items_list)

    except FileNotFoundError:
        return render_template('items.html', items=[])
    except json.JSONDecodeError:
        return render_template('items.html', items=[])
    except Exception as e:
        print(f"Error loading items: {e}")
        return render_template('items.html', items=[])


if __name__ == '__main__':
    app.run(debug=True, port=5000)
