from flask import Flask, current_app, request
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

# Define the directory where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set the UPLOAD_FOLDER configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to generate a unique filename based on current timestamp
def generate_unique_filename(filename):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename_without_extension, extension = os.path.splitext(filename)
    return f"{filename_without_extension}_{current_time}{extension}"

# Function to generate URL for uploaded file
def generate_url(file):
    if file.filename == '':
        return {'error': 'No selected file'}

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = generate_unique_filename(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        # Generate URL for the saved file
        file_url = f"{request.url_root}{UPLOAD_FOLDER}/{unique_filename}" 
        return file_url
    else:
        return {'error': 'File type not allowed'}

if __name__ == '__main__':
    app.run(debug=True)
