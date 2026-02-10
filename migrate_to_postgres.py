#!/usr/bin/env python
"""
Migration script to move from SQLite to PostgreSQL on Render
Run this locally to export your data, then import on Render
"""

import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')
django.setup()

from django.core.management import call_command
from django.db import connections
import json

def export_sqlite_data():
    """Export all data from SQLite to JSON files"""
    print("Exporting data from SQLite...")
    
    # List of apps/models to migrate
    apps_to_migrate = [
        'crypto.CustomUser',
        'crypto.Profile', 
        'crypto.Rank',
        'crypto.Deposit',
        'crypto.Withdrawal',
        'crypto.CopyTrade',
        'crypto.LocalDeposit',
        'crypto.LocalWithdrawal',
        'crypto.Referral',
        'crypto.PromoCode',
        'crypto.PromoRedemption',
        'crypto.DailyReward',
        'crypto.Notification',
    ]
    
    for app_model in apps_to_migrate:
        try:
            app, model = app_model.split('.')
            call_command('dumpdata', f'{app}.{model}', output=f'{model.lower()}_data.json', indent=2)
            print(f"✅ Exported {model}")
        except Exception as e:
            print(f"❌ Failed to export {model}: {e}")

def create_initial_data_script():
    """Create script to run on Render after deployment"""
    script = """#!/bin/bash
# Run this on Render shell after deployment

# Create superuser
python manage.py createsuperuser

# Load initial data (upload JSON files first)
python manage.py loaddata rank_data.json
python manage.py loaddata customuser_data.json
python manage.py loaddata profile_data.json
python manage.py loaddata deposit_data.json
python manage.py loaddata withdrawal_data.json
python manage.py loaddata copytrade_data.json
python manage.py loaddata localdeposit_data.json
python manage.py loaddata localwithdrawal_data.json
python manage.py loaddata referral_data.json
python manage.py loaddata promocode_data.json
python manage.py loadload promoredemption_data.json

# Collect static files
python manage.py collectstatic --noinput

print("Migration completed!")
"""
    
    with open('render_migration.sh', 'w') as f:
        f.write(script)
    
    print("✅ Created render_migration.sh")

if __name__ == '__main__':
    print("🔄 Starting SQLite to PostgreSQL migration preparation...")
    
    # Export current data
    export_sqlite_data()
    
    # Create migration script
    create_initial_data_script()
    
    print("\n📋 Migration Steps:")
    print("1. Upload all *_data.json files to Render")
    print("2. Upload render_migration.sh to Render")
    print("3. Run: chmod +x render_migration.sh")
    print("4. Run: ./render_migration.sh")
    print("\n⚠️  Note: You'll need to recreate superuser manually")
