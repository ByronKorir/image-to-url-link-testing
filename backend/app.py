from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)
app.static_folder = 'uploads'


@app.route('/base64_to_url', methods=['POST'])
def base64_to_url():
    # Get the Base64 data and file name from the request
    base64_data = request.json.get('image')
    file_name = request.json.get('name')

    # Pad the Base64 data if needed
    base64_data += '=' * ((4 - len(base64_data) % 4) % 4)

    # Save the image and get the URL
    url = save_image(base64_data, file_name)

    # Return the URL as JSON response
    return jsonify({'url': url})

    
def save_image(base64_data, file_name):
    # Decode the Base64 data
    decoded_data = base64.b64decode(base64_data)

    # Define a path to save the decoded file
    save_path = 'uploads'
    os.makedirs(save_path, exist_ok=True)

    # Save the decoded file to the local file system
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(decoded_data)

    # Generate a URL that points to the saved file
    url = request.url_root + 'uploads/' + file_name

    # Return the URL
    return url

if __name__ == '__main__':
    app.run(debug=True)
