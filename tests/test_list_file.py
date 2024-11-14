import requests
from cli import list_files
from unittest.mock import patch

def test_list_files():
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = ["file1.txt", "file2.txt"]

        response = list_files()
        assert response == ["file1.txt", "file2.txt"]
        mock_get.assert_called_once_with("http://localhost:8000/files")
