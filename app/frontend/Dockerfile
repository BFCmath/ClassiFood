FROM python:3.9-slim

WORKDIR /app

# Install required system utilities
RUN apt-get update && apt-get install -y \
    sudo \
    dbus

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Disable Streamlit telemetry and set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION
ENV STREAMLIT_TELEMETRY_OPTOUT=true
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Expose the port (optional but good practice)
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]