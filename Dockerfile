# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install fastapi uvicorn scikit-learn numpy pydantic

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
