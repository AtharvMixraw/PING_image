# Image Converter

This is a simple web application to convert images from various formats (JPEG, PNG, BMP, TIFF, RAW, PSD) to PNG. The application is built using Flask for the backend and HTML/CSS for the frontend.

## Features

- Upload images in JPEG, BMP, TIFF, RAW, and PSD formats.
- Convert the uploaded images to PNG format.
- Simple and user-friendly web interface.

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/image-converter.git
    cd image-converter
    ```

2. **Create a virtual environment**:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Ensure you have the necessary libraries**:

    - For **Pillow** to handle image formats:
    
    ```sh
    pip install pillow
    ```

    - For **imageio** to handle RAW images:
    
    ```sh
    pip install imageio
    ```

## Usage

1. **Run the Flask app**:

    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload an image in one of the supported formats and click "Convert" to convert it to PNG.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the web interface.
- `static/`: Directory for static files like CSS.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- Flask
- Pillow
- imageio
- psd-tools

## Example Commands

Here's how to clone the repository, set up the virtual environment, install depe
