#!/bin/bash
# Production Deployment Script for Crypto Investment Platform

set -e

echo "🚀 Starting Production Deployment..."

# Configuration
PROJECT_NAME="crypto_platform"
DEPLOY_USER="deploy"
DEPLOY_PATH="/var/www/$PROJECT_NAME"
BACKUP_PATH="/var/backups/$PROJECT_NAME"
VENV_PATH="$DEPLOY_PATH/venv"
REPO_PATH="$DEPLOY_PATH/repo"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}"
    exit 1
}

warning() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}"
}

# Check if running as deploy user
if [ "$USER" != "$DEPLOY_USER" ]; then
    error "This script must be run as $DEPLOY_USER"
fi

# Create backup
backup() {
    log "Creating backup..."
    mkdir -p $BACKUP_PATH
    sudo -u postgres pg_dump $PROJECT_NAME > "$BACKUP_PATH/backup_$(date +%Y%m%d_%H%M%S).sql"
    log "Backup created successfully"
}

# Update code
update_code() {
    log "Updating code..."
    cd $REPO_PATH
    git pull origin main
    log "Code updated successfully"
}

# Install dependencies
install_dependencies() {
    log "Installing dependencies..."
    source $VENV_PATH/bin/activate
    pip install -r production_requirements.txt
    log "Dependencies installed successfully"
}

# Run migrations
migrate() {
    log "Running database migrations..."
    source $VENV_PATH/bin/activate
    cd $REPO_PATH
    python manage.py migrate --settings=crypto_platform.production_settings
    log "Migrations completed successfully"
}

# Collect static files
collectstatic() {
    log "Collecting static files..."
    source $VENV_PATH/bin/activate
    cd $REPO_PATH
    python manage.py collectstatic --noinput --settings=crypto_platform.production_settings
    log "Static files collected successfully"
}

# Restart services
restart_services() {
    log "Restarting services..."
    sudo systemctl restart gunicorn
    sudo systemctl restart nginx
    sudo systemctl restart redis
    sudo systemctl restart celery
    log "Services restarted successfully"
}

# Health check
health_check() {
    log "Performing health check..."
    sleep 5
    
    # Check if Gunicorn is running
    if ! pgrep -f gunicorn > /dev/null; then
        error "Gunicorn is not running"
    fi
    
    # Check if Nginx is running
    if ! pgrep -f nginx > /dev/null; then
        error "Nginx is not running"
    fi
    
    # Check if the application responds
    if ! curl -f -s http://localhost:8000/ > /dev/null; then
        error "Application is not responding"
    fi
    
    log "Health check passed"
}

# Rollback function
rollback() {
    error "Deployment failed. Rolling back..."
    # Add rollback logic here
    exit 1
}

# Main deployment process
main() {
    log "Starting deployment process..."
    
    # Pre-deployment checks
    if [ ! -d "$REPO_PATH" ]; then
        error "Repository path does not exist: $REPO_PATH"
    fi
    
    if [ ! -d "$VENV_PATH" ]; then
        error "Virtual environment does not exist: $VENV_PATH"
    fi
    
    # Deployment steps
    backup || rollback
    update_code || rollback
    install_dependencies || rollback
    migrate || rollback
    collectstatic || rollback
    restart_services || rollback
    health_check || rollback
    
    log "🎉 Deployment completed successfully!"
    log "Your crypto platform is now live at https://yourdomain.com"
}

# Execute main function
main
