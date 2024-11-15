Here is my dockerfile # Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . /app

# Install pip dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port that Flask will use
EXPOSE 8080

# Start the Flask app
CMD ["python", "app/main.py"]

