# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5000 for the Flask app
EXPOSE 5000:5000

# Define environment variable
ENV NAME game_microservice

# Command to run your application
CMD ["python", "manage.py"]
