"""
Task 2: Flask Logic and Dynamic Routes

Demonstrates Flask logic, URL parameters, and dynamic routing.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/user/<name>')
def greet_user(name):
    """Greet a specific user."""
    return render_template('user.html', name=name)


@app.route('/number/<int:number>')
def check_number(number):
    """Check if a number is even or odd."""
    is_even = number % 2 == 0
    return render_template('number.html', number=number, is_even=is_even)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
