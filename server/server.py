# Import necessary libraries from FastAPI and Python's os module
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from prometheus_client import Counter, generate_latest, start_http_server
from fastapi.responses import PlainTextResponse  # Add this import
import os

# Create an instance of the FastAPI application
app = FastAPI()

# Define the directory where uploaded files will be stored
UPLOAD_FOLDER = "./uploaded_files/"

# Create the upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Define Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
FILE_UPLOAD_COUNT = Counter('files_uploaded_total', 'Total number of files uploaded')
FILE_DELETE_COUNT = Counter('files_deleted_total', 'Total number of files deleted')

# Middleware to count HTTP requests
@app.middleware("http")
async def count_requests(request: Request, call_next):
    """
    Middleware to count the HTTP requests.
    This will increment the `http_requests_total` counter for each request.
    """
    method = request.method
    endpoint = request.url.path
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    response = await call_next(request)
    return response

# Endpoint to upload a file
@app.post("/files/{name}")
async def upload_file(name: str, file: UploadFile = File(...)):
    """
    Uploads a file to the server and saves it in the specified upload folder.
    """
    file_path = os.path.join(UPLOAD_FOLDER, name)

    # Check if the file already exists
    if os.path.exists(file_path):
        raise HTTPException(status_code=409, detail=f"File '{name}' already exists.")

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Increment the upload counter
    FILE_UPLOAD_COUNT.inc()

    return {"message": f"{name} uploaded successfully."}

# Endpoint to delete a specified file
@app.delete("/files/{name}")
async def delete_file(name: str):
    """
    Deletes a file from the server storage if it exists.
    """
    file_path = os.path.join(UPLOAD_FOLDER, name)

    if os.path.exists(file_path):
        os.remove(file_path)

        # Increment the delete counter
        FILE_DELETE_COUNT.inc()

        return {"message": f"{name} deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="File not found")

# Endpoint to list all uploaded files
@app.get("/files")
async def list_files():
    """
    Lists all files currently stored in the upload folder.
    """
    files = os.listdir(UPLOAD_FOLDER)
    return files

# Expose metrics at /metrics route
@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    # This will return the metrics in the Prometheus format
    return generate_latest()
