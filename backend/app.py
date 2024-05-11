from flask import Flask, request, jsonify, send_from_directory
import base64
import os
import uuid
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Serve files from the uploads folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/base64_to_url', methods=['POST'])
def base64_to_url():
    # Get the Base64 data and file name from the request
    base64_data = request.json.get('image')
    file_name = request.json.get('name')

    # Pad the Base64 data if needed
    base64_data += '=' * ((4 - len(base64_data) % 4) % 4)

    # Extract the file extension
    _, file_extension = os.path.splitext(file_name)
    file_extension = file_extension.lstrip('.')  # Remove the leading dot

    # Generate a unique filename
    unique_filename = str(uuid.uuid4()) + '.' + file_extension

    # Save the image and get the URL
    url = save_image(base64_data, unique_filename)

    # Return the URL as JSON response
    # Make sure to remove the trailing slash from request.url_root if present
    url_root = request.url_root.rstrip('/')
    return jsonify({'url': url_root + '/uploads/' + unique_filename})

def save_image(base64_data, filename):
    # Decode the Base64 data
    decoded_data = base64.b64decode(base64_data)

    # Specify the upload directory
    upload_dir = app.config['UPLOAD_FOLDER']
    
    # Ensure the upload directory exists
    os.makedirs(upload_dir, exist_ok=True)

    # Save the decoded file to the upload directory
    file_path = os.path.join(upload_dir, filename)
    with open(file_path, 'wb') as file:
        file.write(decoded_data)

    # Generate a URL that points to the saved file
    url = request.url_root + 'uploads/' + filename

    # Return the URL
    return url

if __name__ == '__main__':
    app.run(debug=True)
