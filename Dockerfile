# PSO+Zscore Trading Application
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y gcc g++ curl && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ .

# Create directories
RUN mkdir -p /app/logs /app/data

# Environment
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Port
EXPOSE ${PORT:-8003}

# Start app
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8003}