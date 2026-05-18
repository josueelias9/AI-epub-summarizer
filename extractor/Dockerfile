# Use Python 3.11 slim image as base
FROM python:3.11-slim


WORKDIR /josue_app
ENV PYTHONPATH=/josue_app

COPY . .

# Install dependencies globally
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create directories for uploads and output
RUN mkdir -p /app/uploads /app/output/images

CMD ["fastapi", "dev", "--host", "0.0.0.0", "--port", "8000", "app/main.py"]
