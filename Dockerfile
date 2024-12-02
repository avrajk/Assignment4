# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the app files into the container
COPY . .

# Step 4: Install the required Python libraries
RUN pip install -r requirements.txt

# Step 5: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 6: Define the command to run the app
CMD ["python", "app.py"]
