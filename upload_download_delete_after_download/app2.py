from flask import Flask, request, send_file, jsonify
import os
import io

app = Flask(__name__)

UPLOAD_FOLDER = 'files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/create', methods=['POST'])
def create_file():
    data = request.get_json()
    filename = data.get('filename')
    content = data.get('content')

    if not filename or not content:
        return jsonify({'error': 'Filename or content missing'}), 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(file_path, 'w') as file:
        file.write(content)

    return jsonify({'message': 'File created successfully'}), 200


@app.route('/download/<filename>', methods=['GET'])
def download_and_delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Create a file-like object
            file_data = io.BytesIO(file.read())

        # Send the file as an attachment
        return send_file(file_data, as_attachment=True, attachment_filename=filename)
    finally:
        # Delete the file after sending
        os.remove(file_path)


if __name__ == '__main__':
    app.run(debug=True)
