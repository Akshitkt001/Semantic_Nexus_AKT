# Use the base image with Python 3.10
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install TensorFlow or PyTorch
RUN pip install tensorflow==2.17.0  # For TensorFlow
# OR
# RUN pip install torch  # For PyTorch

# Copy the rest of your application code
COPY . .

# Run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
