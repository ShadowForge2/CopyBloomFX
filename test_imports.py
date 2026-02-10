"""
Test script to check if imports work
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
    
    # Test imports
    from crypto.models import Rank, Profile
    print("✅ Models import successful")
    
    from crypto.views import dashboard_view
    print("✅ Views import successful")
    
    from crypto.rank_utils import calculate_user_rank
    print("✅ Rank utils import successful")
    
    from crypto.admin import RankAdmin
    print("✅ Admin import successful")
    
    print("\n🎉 All imports successful! Server should start now.")
    
except Exception as e:
    print(f"❌ Import error: {e}")
    import traceback
    traceback.print_exc()
