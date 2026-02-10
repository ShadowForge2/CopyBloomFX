# 🚀 Production Deployment Checklist

## 🔧 Server Setup

### ✅ Server Requirements
- [ ] Ubuntu 20.04+ or CentOS 8+
- [ ] Minimum 2GB RAM, 2 CPU cores
- [ ] 50GB+ SSD storage
- [ ] Static IP address
- [ ] Domain name pointed to server

### ✅ Software Installation
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib redis-server git

# Install Node.js (for build tools if needed)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Certbot for SSL
sudo apt install -y certbot python3-certbot-nginx
```

## 🗄️ Database Setup

### ✅ PostgreSQL Configuration
```bash
# Create database and user
sudo -u postgres psql
CREATE DATABASE crypto_prod;
CREATE USER crypto_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE crypto_prod TO crypto_user;
\q
```

### ✅ Redis Configuration
```bash
# Configure Redis
sudo systemctl enable redis
sudo systemctl start redis
redis-cli ping  # Should return PONG
```

## 🌐 Domain & SSL

### ✅ Domain Configuration
- [ ] DNS A record pointing to server IP
- [ ] Subdomain for admin (optional: admin.yourdomain.com)

### ✅ SSL Certificate
```bash
# Get SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
# Set up auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 📁 Application Setup

### ✅ Deploy User & Directory Structure
```bash
# Create deploy user
sudo adduser deploy
sudo usermod -aG sudo deploy

# Create directory structure
sudo mkdir -p /var/www/crypto_platform
sudo chown deploy:deploy /var/www/crypto_platform

# Clone repository
sudo -u deploy git clone https://github.com/yourusername/crypto-platform.git /var/www/crypto_platform/repo
cd /var/www/crypto_platform/repo

# Create virtual environment
sudo -u deploy python3 -m venv /var/www/crypto_platform/venv
sudo -u deploy /var/www/crypto_platform/venv/bin/pip install -r production_requirements.txt
```

### ✅ Environment Configuration
```bash
# Copy production environment file
sudo -u deploy cp .env.production .env
# Edit with actual values
sudo -u deploy nano .env
```

### ✅ Database Migration
```bash
# Run migrations
sudo -u deploy /var/www/crypto_platform/venv/bin/python manage.py migrate --settings=crypto_platform.production_settings

# Create superuser
sudo -u deploy /var/www/crypto_platform/venv/bin/python manage.py createsuperuser --settings=crypto_platform.production_settings

# Collect static files
sudo -u deploy /var/www/crypto_platform/venv/bin/python manage.py collectstatic --noinput --settings=crypto_platform.production_settings
```

## 🔧 Service Configuration

### ✅ SystemD Services
```bash
# Copy service files
sudo cp gunicorn.service /etc/systemd/system/
sudo cp celery.service /etc/systemd/system/

# Enable and start services
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl enable celery
sudo systemctl start gunicorn
sudo systemctl start celery
```

### ✅ Nginx Configuration
```bash
# Copy Nginx config
sudo cp nginx_config.conf /etc/nginx/sites-available/crypto_platform
sudo ln -s /etc/nginx/sites-available/crypto_platform /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
```

## 🔒 Security Setup

### ✅ Firewall Configuration
```bash
# Configure UFW firewall
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### ✅ Security Updates
```bash
# Install automatic security updates
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

## 📊 Monitoring Setup

### ✅ Log Rotation
```bash
# Create log rotation config
sudo nano /etc/logrotate.d/crypto_platform
```

Content for logrotate file:
```
/var/log/crypto/*.log {
    daily
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 644 www-data www-data
    postrotate
        systemctl reload gunicorn
    endscript
}
```

### ✅ Monitoring Setup
- [ ] Set up Sentry for error tracking
- [ ] Configure Uptime monitoring (Pingdom/UptimeRobot)
- [ ] Set up backup monitoring
- [ ] Configure email alerts for critical errors

## 🔄 Backup Strategy

### ✅ Database Backups
```bash
# Create backup script
sudo nano /usr/local/bin/backup_crypto.sh
```

Content for backup script:
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/crypto_platform"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

# Database backup
pg_dump crypto_prod > $BACKUP_DIR/db_backup_$DATE.sql

# Media files backup
tar -czf $BACKUP_PATH/media_backup_$DATE.tar.gz /var/www/crypto_platform/media/

# Keep only last 7 days
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
```

```bash
# Make executable and schedule
sudo chmod +x /usr/local/bin/backup_crypto.sh
sudo crontab -e
# Add: 0 2 * * * /usr/local/bin/backup_crypto.sh
```

## ✅ Pre-Launch Testing

### ✅ Functionality Tests
- [ ] User registration works
- [ ] Email verification works
- [ ] Login/logout works
- [ ] Deposit functionality works
- [ ] Copy trading works
- [ ] Admin panel accessible
- [ ] Paystack integration works

### ✅ Performance Tests
- [ ] Page load times < 3 seconds
- [ ] Database queries optimized
- [ ] Static files loading correctly
- [ ] SSL certificate valid
- [ ] Mobile responsive

### ✅ Security Tests
- [ ] SQL injection protection
- [ ] XSS protection
- [ ] CSRF protection working
- [ ] Secure headers present
- [ ] No debug information exposed

## 🚀 Launch Day

### ✅ Final Checklist
- [ ] All environment variables set
- [ ] Database migrations run
- [ ] Static files collected
- [ ] SSL certificate installed
- [ ] Services running correctly
- [ ] Monitoring configured
- [ ] Backup strategy active
- [ ] Error tracking enabled

### ✅ Go Live Steps
1. [ ] Update DNS to point to production server
2. [ ] Verify SSL certificate
3. [ ] Test all critical functionalities
4. [ ] Monitor error logs
5. [ ] Announce launch to users

## 📞 Emergency Contacts

### ✅ Support Information
- **Hosting Provider:** [Your hosting provider contact]
- **Domain Registrar:** [Your domain registrar contact]
- **Payment Gateway:** Paystack support
- **Monitoring Service:** [Your monitoring service contact]

---

## 🎯 Post-Launch Tasks

### ✅ First Week
- [ ] Monitor error rates closely
- [ ] Check user feedback
- [ ] Optimize slow queries
- [ ] Verify backup systems working

### ✅ First Month
- [ ] Analyze user behavior
- [ ] Plan feature improvements
- [ ] Review security logs
- [ ] Update documentation

---

**🎉 Your crypto investment platform is ready for production!**
