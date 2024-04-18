# Flask File Management API

This Flask API provides endpoints to create, download, and delete files stored on the server.

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Create a File

Send a POST request to `/create` endpoint with JSON data containing the filename and content to create a file.

Example Request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"filename": "example.txt", "content": "This is some content."}' http://localhost:5000/create
```

### 2. Download a File
Send a GET request to /download/<filename> to download the specified file. The file will be downloaded as an attachment, and it will be deleted from the server after download.

Example Request:
```bash
curl -OJ http://localhost:5000/download/example.txt
```

### 3. Error Handling
If the specified file does not exist, a 404 error will be returned.
If the provided JSON data for file creation is incomplete, a 400 error will be returned.
Configuration
By default, the uploaded files are stored in the files directory. You can change the upload folder location by modifying the UPLOAD_FOLDER variable in the code.

### Development Server
Run the Flask server locally for development:
```
python app.py

```
or
```
python app2.py

```