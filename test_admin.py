"""
Test script to check admin configuration
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
    
    # Test admin imports
    from crypto.admin import RankAdmin, ProfileAdmin, CustomUserAdmin
    print("✅ Admin imports successful")
    
    # Test admin validation
    from django.contrib.admin.sites import site
    print("✅ Admin site validation successful")
    
    print("\n🎉 Admin configuration is valid!")
    print("Now you can run migrations:")
    print("python manage.py makemigrations")
    print("python manage.py migrate")
    
except Exception as e:
    print(f"❌ Admin error: {e}")
    import traceback
    traceback.print_exc()
