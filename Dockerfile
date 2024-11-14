# Use a Python 3.12 slim base image
FROM python:3.12-slim

# Add Metadata
LABEL maintainer="devops-team@example.com>"
LABEL description="Dockerfile for a file storage server application using FastAPI"

# Build arguments to pass UID, GID, and username
ARG USER_NAME=fs-user
ARG USER_ID=1000
ARG GROUP_ID=1000

# Set up environment variables
ENV APP_HOME=/app

# Set up working directory
WORKDIR $APP_HOME

# Installing necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a new group and user with specific UID and GID
RUN groupadd -g $GROUP_ID $USER_NAME && \
    useradd -m -u $USER_ID -g $GROUP_ID -s /bin/bash $USER_NAME

# Copy and install Python dependencies
COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app into the container and own it by fs-user
COPY ./server/ $APP_HOME
RUN chown -R $USER_NAME:$USER_NAME $APP_HOME

# Use fs-store user i.e. non-root user
USER $USER_NAME

# Expose port
EXPOSE 8000

# Run the API server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
