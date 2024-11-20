# Use a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency file into the image
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Create a directory for models
RUN mkdir -p /app/models

# Copy local models folder into the container
COPY models /app/models

# Copy application code into the image
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]
