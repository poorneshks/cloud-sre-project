# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy current directory contents
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "application:app"]
