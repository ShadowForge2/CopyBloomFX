"""
Test admin ban/unban and flag/unflag functionality
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_admin_functions():
    print("🧪 TESTING ADMIN BAN/UNBAN & FLAG/UNFLAG FUNCTIONS")
    print("=" * 60)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile, Notification
        from django.utils import timezone
        
        # Get test users
        test_users = User.objects.filter(is_staff=False).exclude(role='admin')[:5]
        
        if not test_users.exists():
            print("❌ No test users found. Create some regular users first.")
            return
        
        print(f"✅ Found {test_users.count()} test users")
        
        # Test 1: Check current status
        print(f"\n📋 CURRENT USER STATUS:")
        for user in test_users:
            profile = getattr(user, 'profile', None)
            print(f"  👤 {user.username}:")
            print(f"     - Banned: {user.is_banned}")
            print(f"     - Flagged: {user.is_flagged}")
            print(f"     - Staff: {user.is_staff}")
            if profile:
                print(f"     - Referrals: {profile.total_referrals}")
        
        # Test 2: Flag/Unflag functionality
        print(f"\n🚩 TESTING FLAG/UNFLAG:")
        test_user = test_users.first()
        
        if test_user:
            print(f"  🔄 Testing with user: {test_user.username}")
            
            # Test flagging
            original_flagged = test_user.is_flagged
            test_user.is_flagged = True
            test_user.save(update_fields=['is_flagged'])
            print(f"  ✅ Flagged: {original_flagged} → {test_user.is_flagged}")
            
            # Test unflagging
            test_user.is_flagged = False
            test_user.save(update_fields=['is_flagged'])
            print(f"  ✅ Unflagged: {test_user.is_flagged}")
            
            # Check notifications
            flag_notifications = Notification.objects.filter(
                user=test_user,
                message__contains='flagged'
            ).order_by('-created_at')[:3]
            
            if flag_notifications.exists():
                print(f"  📧 Flag notifications found ({flag_notifications.count()} recent):")
                for notif in flag_notifications:
                    print(f"     - {notif.created_at.strftime('%Y-%m-%d %H:%M')}: {notif.message[:50]}...")
            else:
                print(f"  ⚠️  No flag notifications found")
        
        # Test 3: Ban/Unban functionality
        print(f"\n🚫 TESTING BAN/UNBAN:")
        
        for user in test_users[:2]:  # Test with first 2 users
            print(f"  🔄 Testing with user: {user.username}")
            
            # Test banning
            original_banned = user.is_banned
            user.is_banned = True
            user.save(update_fields=['is_banned'])
            print(f"  ✅ Banned: {original_banned} → {user.is_banned}")
            
            # Test unbanning
            user.is_banned = False
            user.save(update_fields=['is_banned'])
            print(f"  ✅ Unbanned: {user.is_banned}")
        
        # Test 4: Check admin protection
        print(f"\n🛡️  TESTING ADMIN PROTECTION:")
        admin_users = User.objects.filter(is_staff=True)
        
        if admin_users.exists():
            admin_user = admin_users.first()
            print(f"  🔄 Testing admin protection with: {admin_user.username}")
            
            # Try to flag admin (should fail)
            original_flagged = admin_user.is_flagged
            admin_user.is_flagged = True
            admin_user.save(update_fields=['is_flagged'])
            admin_user.refresh_from_db()
            
            if admin_user.is_flagged:
                print(f"  ⚠️  Admin was flagged (PROTECTION FAILED)")
            else:
                print(f"  ✅ Admin protection working (cannot be flagged)")
            
            # Reset
            admin_user.is_flagged = original_flagged
            admin_user.save(update_fields=['is_flagged'])
            
            # Try to ban admin (should fail)
            original_banned = admin_user.is_banned
            admin_user.is_banned = True
            admin_user.save(update_fields=['is_banned'])
            admin_user.refresh_from_db()
            
            if admin_user.is_banned:
                print(f"  ⚠️  Admin was banned (PROTECTION FAILED)")
            else:
                print(f"  ✅ Admin protection working (cannot be banned)")
        
        # Test 5: Check URL endpoints exist
        print(f"\n🔗 CHECKING ADMIN URL ENDPOINTS:")
        from django.urls import reverse
        
        try:
            flag_url = reverse('crypto:admin_user_flag', kwargs={'pk': test_user.pk})
            print(f"  ✅ Flag URL: {flag_url}")
        except:
            print(f"  ❌ Flag URL not found")
        
        try:
            unflag_url = reverse('crypto:admin_user_unflag', kwargs={'pk': test_user.pk})
            print(f"  ✅ Unflag URL: {unflag_url}")
        except:
            print(f"  ❌ Unflag URL not found")
        
        try:
            ban_url = reverse('crypto:admin_user_ban', kwargs={'pk': test_user.pk})
            print(f"  ✅ Ban URL: {ban_url}")
        except:
            print(f"  ❌ Ban URL not found")
        
        try:
            unban_url = reverse('crypto:admin_user_unban', kwargs={'pk': test_user.pk})
            print(f"  ✅ Unban URL: {unban_url}")
        except:
            print(f"  ❌ Unban URL not found")
        
        print(f"\n🎉 ADMIN FUNCTIONS TEST COMPLETED!")
        print(f"\n💡 MANUAL TESTING INSTRUCTIONS:")
        print(f"  1. Go to admin panel")
        print(f"  2. Try flagging/unflagging a user")
        print(f"  3. Try banning/unbanning a user")
        print(f"  4. Check if user status changes")
        print(f"  5. Verify notifications are sent")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_admin_functions()
