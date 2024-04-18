from flask import Flask, request, send_file, jsonify, jsonify, after_this_request
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
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    @after_this_request
    def delete_file(response):
        try:
            os.remove(file_path)
        except Exception as e:
            app.logger.error("Error removing file: {}".format(e))
        return response

    with open(file_path, 'rb') as file:
        # Create a file-like object
        file_data = io.BytesIO(file.read())

    # Send the file as an attachment
    return send_file(file_data, as_attachment=True, attachment_filename=filename)



if __name__ == '__main__':
    app.run(debug=True)
