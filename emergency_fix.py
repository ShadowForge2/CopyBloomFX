"""
EMERGENCY FIX - Run this to get the server working immediately
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')
django.setup()

from django.core.management import call_command
from crypto.models import Rank, CustomUser, Profile

def main():
    print("🚀 EMERGENCY DATABASE FIX")
    print("=" * 50)
    
    try:
        # Step 1: Create migrations for current models
        print("\n1. Creating migrations...")
        call_command('makemigrations', '--noinput')
        print("✅ Migrations created")
        
        # Step 2: Apply migrations
        print("\n2. Applying migrations...")
        call_command('migrate', '--noinput')
        print("✅ Migrations applied")
        
        # Step 3: Seed ranks with correct field names
        print("\n3. Seeding ranks...")
        RANKS = [
            {'name': 'Green Horn', 'min_balance': 7, 'max_balance': 49, 'daily_profit_percentage': 1.67, 'max_copy_trades': 1, 'color': '#4CAF50'},
            {'name': 'Student Form', 'min_balance': 50, 'max_balance': 100, 'daily_profit_percentage': 2.0, 'max_copy_trades': 2, 'color': '#2196F3'},
            {'name': 'Market Maven', 'min_balance': 100, 'max_balance': 500, 'daily_profit_percentage': 2.0, 'max_copy_trades': 3, 'color': '#9C27B0'},
            {'name': 'Gunslinger', 'min_balance': 500, 'max_balance': 1500, 'daily_profit_percentage': 2.2, 'max_copy_trades': 4, 'color': '#FF9800'},
            {'name': 'Whale', 'min_balance': 1500, 'max_balance': 5000, 'daily_profit_percentage': 2.5, 'max_copy_trades': 5, 'color': '#FFC107'},
            {'name': 'Market Wizard', 'min_balance': 5000, 'max_balance': None, 'daily_profit_percentage': 2.7, 'max_copy_trades': 6, 'color': '#FFD700'},
        ]
        
        for rank_data in RANKS:
            rank, created = Rank.objects.update_or_create(
                name=rank_data['name'],
                defaults=rank_data
            )
            if created:
                print(f"  ✅ Created rank: {rank.name}")
            else:
                print(f"  ✅ Updated rank: {rank.name}")
        
        print("\n🎉 EMERGENCY FIX COMPLETED!")
        print("\n📋 What was fixed:")
        print("  ✅ Database schema updated")
        print("  ✅ Rank field names corrected")
        print("  ✅ Ranks seeded with correct data")
        print("  ✅ Server should now start without errors")
        
        print("\n🚀 Now try running:")
        print("  python manage.py runserver")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
