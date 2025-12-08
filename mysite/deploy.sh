#!/bin/bash

# Simple Deployment Script for DigitalOcean
# No Nginx, just Django + Gunicorn

set -e

echo "🚀 Starting simple deployment..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found"
    echo "Please create a .env file manually on the server based on .env.example"
    exit 1
fi

# Build and start
echo "🔨 Building Docker image..."
docker compose -f docker-compose.prod.yml build

echo "🛑 Stopping existing containers..."
docker compose -f docker-compose.prod.yml down

echo "🚀 Starting container..."
docker compose -f docker-compose.prod.yml up -d

# Wait for service to start
echo "⏳ Waiting for service to start..."
sleep 5

# Run migrations
echo "🔄 Running database migrations..."
docker compose -f docker-compose.prod.yml exec -T web python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
docker compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput

# Show status
echo "✅ Deployment completed!"
echo "📊 Container status:"
docker compose -f docker-compose.prod.yml ps

echo ""
echo "🎉 Your app is running!"
echo "Visit: http://$(curl -s ifconfig.me)"
