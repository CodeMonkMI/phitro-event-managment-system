# Stage 1: build Tailwind CSS assets using Node
FROM node:22-alpine AS node_builder

WORKDIR /build

# enable corepack (pnpm via corepack) and install deps
RUN corepack enable && corepack prepare pnpm@latest --activate

# copy frontend files (only what we need to build CSS)
COPY package.json pnpm-lock.yaml ./ 
COPY static/css/input.css static/css/input.css

RUN pnpm install --frozen-lockfile --prod=false
RUN pnpm run build

# Stage 2: Python runtime for Django application
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/venv/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Python packages (e.g., psycopg2)
# and for building other requirements.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment and activate it
RUN python -m venv /venv

# Copy Python requirements file and install them
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Copy built static CSS from the node_builder stage
COPY --from=node_builder /build/static/css/output.css /app/static/css/output.css

# Make the entrypoint script executable
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Set Django settings module
ENV DJANGO_SETTINGS_MODULE=evms.settings

# Expose the port Django will run on
EXPOSE 8000

# Define the entrypoint script to be executed when the container starts
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

# Define the default command to run the Django application with Gunicorn
CMD ["gunicorn", "evms.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
