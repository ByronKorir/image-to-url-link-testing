from flask import Flask, request, jsonify, send_from_directory

from flask_cors import CORS
from views import *

app = Flask(__name__)
CORS(app)

app.register_blueprint(file_bp)


# Route to serve saved images
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    UPLOAD_FOLDER = 'uploads'  # Define the upload folder here or import it from your configuration
    return send_from_directory(UPLOAD_FOLDER, filename)



if __name__ == '__main__':
    app.run(debug=True)
