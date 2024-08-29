# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir prometheus_client flask

# Expose port 8000 for Prometheus metrics and 5000 for the Flask app
EXPOSE 8000
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
