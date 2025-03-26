# Use the appropriate base image
FROM python:3.11.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy the .env file into the container
COPY .env .env

# Ensure python-dotenv is installed (add this to requirements.txt if not already present)
RUN pip install python-dotenv

# Set environment variables (optional, for local testing)
ENV DATABASE_URL=${DATABASE_URL}

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
