# Dockerfile

# Start with a Python base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# !! Explicitly create the Images directory !!
RUN mkdir Images

# Install OS dependencies for OpenCV
# This command adds the missing libGL.so.1 library.
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker's build cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire project into the working directory.
# This will create /app/carDetectionModel, /app/Images, etc.
COPY . .

# Set the command to run your main script when the container starts.
CMD ["python", "carDetectionModel/mqtt.py"]