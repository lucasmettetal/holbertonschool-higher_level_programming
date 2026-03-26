"""
Task 3: File Handling in Flask

Demonstrates file operations and serving files in Flask.
"""

from flask import Flask, render_template, send_file
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')


@app.route('/files')
def list_files():
    """List all files in uploads folder."""
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('files.html', files=files)


@app.route('/download/<filename>')
def download_file(filename):
    """Download a file from uploads folder."""
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return 'File not found', 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
