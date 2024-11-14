import requests
from cli import delete_file
from unittest.mock import patch

def test_delete_file():
    with patch('requests.delete') as mock_delete:
        mock_delete.return_value.status_code = 200
        mock_delete.return_value.json.return_value = {"message": "File deleted successfully"}

        response = delete_file("testfile.txt")
        assert response == {"message": "File deleted successfully"}
        mock_delete.assert_called_once_with("http://localhost:8000/files/testfile.txt")
