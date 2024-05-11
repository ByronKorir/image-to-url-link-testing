from flask import  Blueprint, request, jsonify
from upload_images import generate_url


file_bp = Blueprint('file_bp', __name__)

# Route to handle file upload
@file_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    file_url = generate_url(file)  # Pass the Flask application instance
    return jsonify({'file_url': file_url})


