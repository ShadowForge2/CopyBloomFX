"""
PROPER MIGRATION PLAN - Run this after site is stable
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def run_proper_migration():
    print("🚀 PROPER MIGRATION PLAN")
    print("=" * 50)
    
    print("\n📋 STEP 1: Update models to new field names")
    print("   - Change daily_profit_pct to daily_profit_percentage")
    print("   - Change copy_trades_limit to max_copy_trades")
    print("   - Uncomment last_daily_profit_at field")
    print("   - Uncomment DailyProfit model")
    
    print("\n📋 STEP 2: Create migration")
    print("   python manage.py makemigrations crypto")
    
    print("\n📋 STEP 3: Apply migration")
    print("   python manage.py migrate")
    
    print("\n📋 STEP 4: Update code to use new field names")
    print("   - Update views.py to use new field names")
    print("   - Update admin.py to use new field names")
    print("   - Remove property aliases from models")
    
    print("\n📋 STEP 5: Test everything")
    print("   - Test dashboard")
    print("   - Test admin interface")
    print("   - Test copy trades")
    print("   - Test daily profit")
    
    print("\n⚠️  WARNING: Backup your database before running migrations!")
    print("   cp db.sqlite3 db.sqlite3.backup")
    
    print("\n🎯 CURRENT STATUS: Site is working with old field names")
    print("🎯 NEXT STEP: Run proper migration when ready")

if __name__ == "__main__":
    run_proper_migration()
