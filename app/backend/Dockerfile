FROM python:3.9-slim

WORKDIR /app

# Install dependencies for downloading weights
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    python3-pip \
    && apt-get clean

# Install the Kaggle CLI
RUN pip install kaggle --no-cache-dir

# Copy the weight download script into the container
COPY download_weights.sh /app/download_weights.sh

# Make the script executable
RUN chmod +x /app/download_weights.sh

# Run the weight download script to set up files and directories
RUN bash /app/download_weights.sh

# Copy dependency list early for better caching
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application structure for debugging
COPY . .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
