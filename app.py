from flask import Flask, request, redirect, url_for, send_file, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import os
from psd_tools import PSDImage
import rawpy
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        output_filename = filename.rsplit('.', 1)[0] + '.png'
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
        convert_to_png(input_path, output_path)
        return send_file(output_path, as_attachment=True)
    return redirect(request.url)

def convert_to_png(input_path, output_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.png']:
        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')
    elif ext == '.psd':
        psd = PSDImage.open(input_path)
        psd.composite().save(output_path)
    elif ext in ['.raw', '.nef', '.cr2']:  # Add other raw formats if needed
        with rawpy.imread(input_path) as raw:
            rgb = raw.postprocess()
            img = Image.fromarray(rgb)
            img.save(output_path, 'PNG')
    else:
        raise ValueError("Unsupported file format")

if __name__ == '__main__':
    app.run(debug=True)
