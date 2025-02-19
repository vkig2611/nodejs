# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the app files
COPY app.py .

# Expose a port (optional, useful for testing)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
