# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model and inference script
COPY model.pkl .
COPY inference.py .

# Create directories for input and output (optional, but good practice)
RUN mkdir -p /input/logs /output

# Define the command to run the inference script
CMD ["python", "inference.py"]
