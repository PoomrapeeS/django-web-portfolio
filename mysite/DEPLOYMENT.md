# DigitalOcean Deployment Guide

Simple deployment for learning - just Django + Gunicorn with WhiteNoise for static files.

## Prerequisites

- DigitalOcean Droplet (Ubuntu 22.04)
- SSH access

## 1️⃣ Setup Droplet

```bash
# SSH into droplet
ssh root@YOUR_DROPLET_IP

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Docker Compose
apt install docker-compose -y

# Create project directory
mkdir -p /var/www/django-portfolio
cd /var/www/django-portfolio
```

## 2️⃣ Upload Files

**Option A: Using SCP (from your Windows machine)**
```bash
cd "c:/Users/poomr/OneDrive - The Gang Technology Co., Ltd/Projects/django-web-portfolio/mysite"
scp -r * root@YOUR_DROPLET_IP:/var/www/django-portfolio/
```

**Option B: Using Git (recommended)**
```bash
# On droplet:
cd /var/www/django-portfolio
git clone YOUR_GITHUB_REPO .
```

## 3️⃣ Configure Environment

```bash
cd /var/www/django-portfolio

# Create .env file
cp .env.example .env
nano .env
```

**Edit `.env`:**
```env
SECRET_KEY=GENERATE_NEW_SECRET_KEY_HERE
DEBUG=False
ALLOWED_HOSTS=YOUR_DROPLET_IP
```

**Generate SECRET_KEY:**
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## 4️⃣ Deploy

```bash
# Build and start
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d

# Run migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate

# Create admin user
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

# Collect static files
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

## 5️⃣ Open Firewall

```bash
ufw allow 22/tcp   # SSH
ufw allow 80/tcp   # HTTP
ufw enable
```

## 6️⃣ Test

Visit: `http://YOUR_DROPLET_IP`

## 🔄 Update Your App

```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d

# Run migrations if needed
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
```

Or use the deploy script:
```bash
chmod +x deploy.sh
./deploy.sh
```

## 📝 Useful Commands

**View logs:**
```bash
docker-compose -f docker-compose.prod.yml logs -f
```

**Restart:**
```bash
docker-compose -f docker-compose.prod.yml restart
```

**Stop:**
```bash
docker-compose -f docker-compose.prod.yml down
```

**Django shell:**
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py shell
```

**Create superuser:**
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

## 🐛 Troubleshooting

**Container won't start?**
```bash
docker-compose -f docker-compose.prod.yml logs
```

**Static files not loading?**
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
docker-compose -f docker-compose.prod.yml restart
```

**Check container status:**
```bash
docker-compose -f docker-compose.prod.yml ps
docker ps
```

## ⚠️ Note

This setup is simplified for learning:
- Uses WhiteNoise for static files (no separate web server needed)
- No HTTPS/SSL (use a reverse proxy like Cloudflare or add Nginx later for SSL)
- Great for learning and small projects

---

**That's it! Simple deployment. 🎉**
