# syntax=docker/dockerfile:1

FROM python:3

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependancies.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to the container image.
COPY . .
