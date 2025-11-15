# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code (app.py, static, templates)
COPY . .

# Create the data directory so Gunicorn can write to it
RUN mkdir -p /app/data

# Tell Docker what command to run when the container starts
# We use Gunicorn to serve the app (app:app means "in file app.py, find the variable app")
# We bind to 0.0.0.0:5000 so it's accessible within the Docker network
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:5000", "app:app"]
