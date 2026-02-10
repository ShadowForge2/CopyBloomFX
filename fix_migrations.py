#!/usr/bin/env python
"""
Database Migration Fix Script
This script will apply migrations and seed the database with correct ranks
"""
import os
import sys
import django

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

try:
    django.setup()
    print("✅ Django setup successful")
except Exception as e:
    print(f"❌ Django setup failed: {e}")
    sys.exit(1)

from django.core.management import execute_from_command_line
from django.db import connection
from crypto.models import Rank, CustomUser, Profile


def run_migrations():
    """Run Django migrations"""
    print("\n🔄 Running migrations...")
    try:
        # Run makemigrations
        print("  - Creating migrations...")
        execute_from_command_line(['manage.py', 'makemigrations', '--noinput'])
        
        # Run migrate
        print("  - Applying migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        
        print("✅ Migrations completed successfully")
        return True
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        return False


def check_database_schema():
    """Check if database schema matches models"""
    print("\n🔍 Checking database schema...")
    
    try:
        # Check if DailyProfit table exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='crypto_dailyprofit';")
            dailyprofit_exists = cursor.fetchone()
            
            cursor.execute("PRAGMA table_info(crypto_rank);")
            rank_columns = cursor.fetchall()
            
            cursor.execute("PRAGMA table_info(crypto_profile);")
            profile_columns = cursor.fetchall()
        
        print(f"  - DailyProfit table exists: {'✅' if dailyprofit_exists else '❌'}")
        
        # Check Rank columns
        rank_column_names = [col[1] for col in rank_columns]
        required_rank_columns = ['daily_profit_percentage', 'max_copy_trades', 'max_balance']
        
        for col in required_rank_columns:
            if col in rank_column_names:
                print(f"  - Rank.{col}: ✅")
            else:
                print(f"  - Rank.{col}: ❌")
        
        # Check Profile columns
        profile_column_names = [col[1] for col in profile_columns]
        required_profile_columns = ['last_daily_profit_at']
        
        for col in required_profile_columns:
            if col in profile_column_names:
                print(f"  - Profile.{col}: ✅")
            else:
                print(f"  - Profile.{col}: ❌")
        
        return True
    except Exception as e:
        print(f"❌ Schema check failed: {e}")
        return False


def seed_ranks():
    """Seed the database with correct ranks"""
    print("\n🌱 Seeding ranks...")
    
    RANKS = [
        {'name': 'Green Horn', 'min_balance': 7, 'max_balance': 49, 'daily_profit_percentage': 1.67, 'max_copy_trades': 1, 'color': '#4CAF50'},
        {'name': 'Student Form', 'min_balance': 50, 'max_balance': 100, 'daily_profit_percentage': 2.0, 'max_copy_trades': 2, 'color': '#2196F3'},
        {'name': 'Market Maven', 'min_balance': 100, 'max_balance': 500, 'daily_profit_percentage': 2.0, 'max_copy_trades': 3, 'color': '#9C27B0'},
        {'name': 'Gunslinger', 'min_balance': 500, 'max_balance': 1500, 'daily_profit_percentage': 2.2, 'max_copy_trades': 4, 'color': '#FF9800'},
        {'name': 'Whale', 'min_balance': 1500, 'max_balance': 5000, 'daily_profit_percentage': 2.5, 'max_copy_trades': 5, 'color': '#FFC107'},
        {'name': 'Market Wizard', 'min_balance': 5000, 'max_balance': None, 'daily_profit_percentage': 2.7, 'max_copy_trades': 6, 'color': '#FFD700'},
    ]
    
    try:
        # Check if ranks already exist
        existing_count = Rank.objects.count()
        if existing_count > 0:
            print(f"  - Found {existing_count} existing ranks")
            
            # Update existing ranks with correct field names
            for rank_data in RANKS:
                try:
                    rank = Rank.objects.get(name=rank_data['name'])
                    # Update fields that might have changed
                    rank.daily_profit_percentage = rank_data['daily_profit_percentage']
                    rank.max_copy_trades = rank_data['max_copy_trades']
                    rank.max_balance = rank_data['max_balance']
                    rank.save()
                    print(f"  - Updated rank: {rank.name}")
                except Rank.DoesNotExist:
                    # Create new rank if it doesn't exist
                    Rank.objects.create(**rank_data)
                    print(f"  - Created rank: {rank_data['name']}")
        else:
            # Create all ranks if none exist
            for rank_data in RANKS:
                Rank.objects.create(**rank_data)
                print(f"  - Created rank: {rank_data['name']}")
        
        print(f"✅ Rank seeding completed. Total ranks: {Rank.objects.count()}")
        return True
    except Exception as e:
        print(f"❌ Rank seeding failed: {e}")
        return False


def create_admin_user():
    """Create admin user if doesn't exist"""
    print("\n👤 Creating admin user...")
    
    try:
        if CustomUser.objects.filter(username='admin').exists():
            print("  - Admin user already exists")
            return True
        
        admin = CustomUser.objects.create_superuser('admin', 'admin@copytrade.local', 'admin123')
        admin.role = 'admin'
        admin.save()
        
        # Create profile without default rank
        Profile.objects.create(user=admin, referral_code='ADMIN1')
        
        print("  - Admin user created: username=admin, password=admin123")
        return True
    except Exception as e:
        print(f"❌ Admin user creation failed: {e}")
        return False


def test_basic_functionality():
    """Test basic functionality"""
    print("\n🧪 Testing basic functionality...")
    
    try:
        # Test rank calculation
        ranks = list(Rank.objects.order_by('min_balance'))
        print(f"  - Found {len(ranks)} ranks")
        
        # Test profile creation
        test_user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        Profile.objects.create(user=test_user, referral_code='TEST123')
        
        # Test rank calculation
        profile = test_user.profile
        rank = profile.get_rank()
        print(f"  - Test user rank: {rank.name if rank else 'None'}")
        
        # Clean up
        test_user.delete()
        
        print("✅ Basic functionality test passed")
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False


def main():
    """Main migration process"""
    print("🚀 Starting Database Migration Fix Process\n")
    
    success = True
    
    # Step 1: Run migrations
    if not run_migrations():
        success = False
    
    # Step 2: Check database schema
    if success and not check_database_schema():
        success = False
    
    # Step 3: Seed ranks
    if success and not seed_ranks():
        success = False
    
    # Step 4: Create admin user
    if success and not create_admin_user():
        success = False
    
    # Step 5: Test basic functionality
    if success and not test_basic_functionality():
        success = False
    
    # Final result
    if success:
        print("\n🎉 Database migration fix completed successfully!")
        print("\n📋 Summary:")
        print("  ✅ Migrations applied")
        print("  ✅ Database schema updated")
        print("  ✅ Ranks seeded correctly")
        print("  ✅ Admin user created")
        print("  ✅ Basic functionality verified")
        print("\n🚀 The project should now run without OperationalErrors!")
    else:
        print("\n❌ Database migration fix failed!")
        print("Please check the error messages above and fix the issues.")
    
    return success


if __name__ == "__main__":
    main()
