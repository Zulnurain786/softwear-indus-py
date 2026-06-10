# Use the required base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies (including mysql-connector-python or flask-mysqldb)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project code
COPY . .

# Expose the port your Flask app runs on (matching the exercise)
EXPOSE 80

# Command to run your application
CMD ["python", "run.py"]