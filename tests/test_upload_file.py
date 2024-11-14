import requests
from cli import upload_file
from unittest.mock import patch

def test_upload_file_success():
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "File uploaded successfully"}

        response = upload_file("/path/to/testfile.txt")
        assert response == {"message": "File uploaded successfully"}
        mock_post.assert_called_once_with(
            "http://localhost:8000/files/testfile.txt",
            files={"file": open("/path/to/testfile.txt", 'rb')}
        )

def test_upload_file_conflict():
    # Simulate the case where the file already exists and the server returns a 409 Conflict error
    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 409
        mock_post.return_value.json.return_value = {"detail": "File 'testfile.txt' already exists."}

        response = upload_file("/path/to/testfile.txt")
        assert response == {"detail": "File 'testfile.txt' already exists."}
        mock_post.assert_called_once_with(
            "http://localhost:8000/files/testfile.txt",
            files={"file": open("/path/to/testfile.txt", 'rb')}
        )
