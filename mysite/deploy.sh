#!/bin/bash

# Simple Deployment Script for DigitalOcean
# No Nginx, just Django + Gunicorn

set -e

echo "🚀 Starting simple deployment..."

# Create .env file from environment variables if they exist
if [ -n "$USE_POSTGRES" ] || [ -n "$SECRET_KEY" ]; then
    echo "📝 Creating .env file from environment variables..."
    cat > .env << EOF
USE_POSTGRES=${USE_POSTGRES:-False}
POSTGRES_DB=${POSTGRES_DB:-portfolio}
POSTGRES_USER=${POSTGRES_USER:-postgres}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-changeme}
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}
SECRET_KEY=${SECRET_KEY:-django-insecure-change-this}
DEBUG=${DEBUG:-False}
ALLOWED_HOSTS=${ALLOWED_HOSTS:-localhost,127.0.0.1}
EOF
    echo "✅ .env file created"
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found"
    echo "Please create a .env file based on .env.example or set environment variables"
    exit 1
fi

# Build and start
echo "🔨 Building Docker image..."
docker-compose -f docker-compose.prod.yml build

echo "🛑 Stopping existing containers..."
docker-compose -f docker-compose.prod.yml down

echo "🚀 Starting container..."
docker-compose -f docker-compose.prod.yml up -d

# Wait for service to start
echo "⏳ Waiting for service to start..."
sleep 5

# Run migrations
echo "🔄 Running database migrations..."
docker-compose -f docker-compose.prod.yml exec -T web python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
docker-compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput

# Show status
echo "✅ Deployment completed!"
echo "📊 Container status:"
docker-compose -f docker-compose.prod.yml ps

echo ""
echo "🎉 Your app is running!"
echo "Visit: http://$(curl -s ifconfig.me)"
