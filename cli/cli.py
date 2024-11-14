# Import necessary libraries
import click        # For creating command-line interface commands
import requests     # For making HTTP requests to the file-storage server

# Define the base URL for the file-storage server
SERVER_URL = "http://localhost:8000"

# Create a Click group to serve as the main entry point for CLI commands
@click.group()
def cli():
    """
    A command-line interface for interacting with the file-storage server.
    """
    pass

# Define the command for uploading a file
@cli.command("upload-file")
@click.argument("file_path")
def upload_file(file_path):
    """
    Uploads a file to the server.
    
    Parameters:
    - file_path (str): Path to the file to be uploaded.
    
    Sends a POST request to the server with the file contents.
    """
    # Extract the file name from the provided file path
    file_name = file_path.split("/")[-1]

    # Open the file in binary mode and send it in a POST request
    with open(file_path, "rb") as f:
        # Make a POST request to the server, sending the file as multipart/form-data
        response = requests.post(f"{SERVER_URL}/files/{file_name}", files={"file": f})
        
        # Print the server's response to the command line
        click.echo(response.json())

# Define the command for deleting a file
@cli.command("delete-file")
@click.argument("file_name")
def delete_file(file_name):
    """
    Deletes a specified file from the server.
    
    Parameters:
    - file_name (str): Name of the file to be deleted.
    
    Sends a DELETE request to the server to remove the specified file.
    """
    # Make a DELETE request to the server with the specified file name
    response = requests.delete(f"{SERVER_URL}/files/{file_name}")

    # Print the server's response to the command line
    click.echo(response.json())

# Define the command for listing all files on the server
@cli.command("list-files")
def list_files():
    """
    Lists all files currently stored on the server.
    
    Sends a GET request to the server to retrieve the list of files.
    """
    # Make a GET request to retrieve the list of files
    response = requests.get(f"{SERVER_URL}/files")

    # Print the server's response to the command line
    click.echo(response.json())

# Main entry point for the CLI application
if __name__ == "__main__":
    cli()
