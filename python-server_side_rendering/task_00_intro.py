"""
Task 0: Introduction to Flask

A simple introduction to Flask framework and basic routing.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Simple hello route."""
    return 'Hello from Flask!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
