"""
Test script to verify profile picture upload and debug issues
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_profile_picture_upload():
    print("TESTING PROFILE PICTURE UPLOAD SYSTEM")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.conf import settings
        from django.contrib.auth.models import User
        from crypto.models import Profile
        
        print(f"✅ Django setup successful")
        
        # Check MEDIA configuration
        print(f"\n📁 Media Configuration:")
        print(f"  - MEDIA_ROOT: {getattr(settings, 'MEDIA_ROOT', 'Not set')}")
        print(f"  - MEDIA_URL: {getattr(settings, 'MEDIA_URL', 'Not set')}")
        
        # Check if media directory exists
        media_root = getattr(settings, 'MEDIA_ROOT', None)
        if media_root:
            if os.path.exists(media_root):
                print(f"  - Media directory exists: ✅")
                print(f"  - Media path: {media_root}")
            else:
                print(f"  - Media directory exists: ❌")
                print(f"  - Creating media directory...")
                os.makedirs(media_root, exist_ok=True)
                print(f"  - Media directory created: ✅")
        else:
            print(f"  - MEDIA_ROOT not configured: ❌")
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"\n✅ Testing with user: {test_user.username}")
        
        profile = test_user.profile
        
        print(f"\n📊 Profile Picture Status:")
        if profile.profile_picture:
            print(f"  - Has profile picture: ✅")
            print(f"  - Stored path: {profile.profile_picture}")
            
            # Check if file actually exists
            if media_root:
                full_path = os.path.join(media_root, profile.profile_picture)
                if os.path.exists(full_path):
                    print(f"  - File exists: ✅")
                    print(f"  - Full path: {full_path}")
                    file_size = os.path.getsize(full_path)
                    print(f"  - File size: {file_size} bytes")
                else:
                    print(f"  - File exists: ❌")
                    print(f"  - Expected path: {full_path}")
        else:
            print(f"  - Has profile picture: ❌")
            print(f"  - Status: No picture uploaded")
        
        # Check profile_pics directory
        if media_root:
            profile_pics_dir = os.path.join(media_root, 'profile_pics')
            if os.path.exists(profile_pics_dir):
                print(f"\n📁 Profile Pictures Directory:")
                print(f"  - Directory exists: ✅")
                print(f"  - Path: {profile_pics_dir}")
                
                # List files in directory
                files = os.listdir(profile_pics_dir)
                if files:
                    print(f"  - Files in directory: {len(files)}")
                    for file in files[:5]:  # Show first 5 files
                        file_path = os.path.join(profile_pics_dir, file)
                        file_size = os.path.getsize(file_path)
                        print(f"    * {file} ({file_size} bytes)")
                else:
                    print(f"  - Files in directory: 0")
            else:
                print(f"\n📁 Profile Pictures Directory:")
                print(f"  - Directory exists: ❌")
                print(f"  - Creating directory...")
                os.makedirs(profile_pics_dir, exist_ok=True)
                print(f"  - Directory created: ✅")
        
        print(f"\n🔧 Debugging Tips:")
        print(f"  1. Check MEDIA_ROOT in settings.py")
        print(f"  2. Ensure media directory is writable")
        print(f"  3. Check form validation errors")
        print(f"  4. Verify file upload permissions")
        print(f"  5. Check browser console for errors")
        
        print(f"\n✅ Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_profile_picture_upload()
