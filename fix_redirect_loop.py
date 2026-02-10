"""
Quick fix for redirect loop issue
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
    
    from django.contrib.auth.models import User
    from crypto.models import Profile
    
    print("🔧 Fixing redirect loop issues...")
    
    # Check if admin user exists and has profile
    admin_user = User.objects.filter(username='admin').first()
    if admin_user:
        print(f"✅ Admin user found: {admin_user.username}")
        
        # Check if admin has profile
        profile = Profile.objects.filter(user=admin_user).first()
        if not profile:
            print("⚠️  Admin user missing profile - creating one...")
            profile = Profile.objects.create(user=admin_user, referral_code='ADMIN123')
            print(f"✅ Created profile for admin: {profile.referral_code}")
        else:
            print(f"✅ Admin profile exists: {profile.referral_code}")
    
    # Check regular users
    regular_users = User.objects.filter(is_staff=False, is_superuser=False)
    print(f"\n📊 Found {regular_users.count()} regular users")
    
    for user in regular_users:
        profile = Profile.objects.filter(user=user).first()
        if not profile:
            print(f"⚠️  Creating profile for user: {user.username}")
            Profile.objects.create(user=user, referral_code=f'USER{user.id}')
    
    print("\n🎉 Redirect loop fix completed!")
    print("Now try accessing the site again.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
