"""
Test if the site works with old field names
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

try:
    import django
    django.setup()
    print("✅ Django setup successful")
    
    # Test model imports
    from crypto.models import Rank, Profile, CustomUser
    print("✅ Models import successful")
    
    # Test rank functionality
    ranks = Rank.objects.all()
    print(f"✅ Found {ranks.count()} ranks")
    
    for rank in ranks:
        print(f"  - {rank.name}: {rank.daily_profit_pct}% profit, {rank.copy_trades_limit} trades")
        # Test property aliases
        print(f"    Alias test: {rank.daily_profit_percentage}% profit, {rank.max_copy_trades} trades")
    
    # Test profile functionality
    profiles = Profile.objects.all()
    print(f"✅ Found {profiles.count()} profiles")
    
    print("\n🎉 Site should work now!")
    print("Try accessing: http://127.0.0.1:8000/")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
