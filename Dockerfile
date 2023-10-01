# Use a smaller base image, like Alpine Linux
FROM python:3.9-slim-buster as base

# Set environment variables for Python to optimize for production
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy just the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Switch to a second stage for the final image
FROM base as final

# Copy the FastAPI application code into the container
COPY . .

# Expose port 80 for the FastAPI app
EXPOSE 80

# Define the command to run the FastAPI app
CMD ["uvicorn", "imges_fast:app", "--host", "0.0.0.0", "--port", "80"]
