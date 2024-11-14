# File Storage Server and CLI in Python
A simple File Storage Server with CLI

This project provides a simple file storage server written in Python with a command-line interface (CLI) for uploading, listing, and deleting files.

# Build and Run the server locally, please follow below procedure.
## Installation
#### Note: Please download or git clone repository and be in directory file-storage-server.

### Run with Docker
1. Build the docker container image:
   ```bash
   docker build -t file-storage-server .
   ```

2. Create the docker container for file-storage-server:
   ```bash
   docker run -d -p 8000:8000 file-storage-server
   ```

3. This will run file-storage-server on port `8000` locally.

### Monitoring with Prometheus

To enable monitoring and metrics collection, the server integrates with **Prometheus** for tracking various operational statistics.

- **Metrics Exposed**: The server exposes the following metrics:
  - **Number of files uploaded**: Tracks how many files have been uploaded.
  - **Number of files deleted**: Tracks how many files have been deleted.
  - **Number of HTTP requests**: Tracks the total number of HTTP requests received by the server, categorized by HTTP method and endpoint.

- **Metrics Endpoint**: The metrics are exposed on the `/metrics` endpoint, available on the same port where the FastAPI server is running. By default, the metrics are available at:
  ```bash
  http://localhost:8000/metrics


### Install CLI Locally
1. Install the CLI tool:
   ```bash
   cd cli/
   pip install -e .
   ```

## Usage

Once the CLI is installed, use it to interact with the server:
We can use `fs-store` command to do file operations.

- **Upload a file**:
  ```bash
  fs-store upload-file /path/to/yourfile.txt
  ```

- **List files**:
  ```bash
  fs-store list-files
  ```

- **Delete a file**:
  ```bash
  fs-store delete-file yourfile.txt
  ```

## Pre-commit Hooks

This repository uses **pre-commit hooks** to ensure code quality, enforce coding standards, and automatically fix common issues before code is committed to the repository. 
The pre-commit framework is a tool to manage and maintain multi-language pre-commit hooks.
### Check .pre-commit-config.yaml for more details.
