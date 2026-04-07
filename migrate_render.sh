#!/bin/bash
# DATABASE MIGRATION SCRIPT FOR RENDER DEPLOYMENT

echo "🚀 Starting database migration for Render deployment..."

# Check if we're on Render
if [ -n "$RENDER_EXTERNAL_HOSTNAME" ]; then
    echo "✅ Detected Render environment"
    
    # Create migrations if they don't exist
    echo "📝 Creating migrations..."
    python manage.py makemigrations
    
    # Apply migrations
    echo "🔄 Applying migrations..."
    python manage.py migrate
    
    # Create superuser (optional - remove if not needed)
    echo "👤 Creating superuser..."
    python manage.py shell << EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'your-secure-password')
    print('✅ Superuser created')
else:
    print('ℹ️ Superuser already exists')
EOF
    
    # Collect static files
    echo "📁 Collecting static files..."
    python manage.py collectstatic --noinput
    
    echo "🎉 Migration completed successfully!"
else
    echo "❌ Not in Render environment. Skipping migration."
fi
