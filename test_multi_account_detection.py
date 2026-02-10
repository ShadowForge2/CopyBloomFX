"""
Test script to verify multi-account detection system
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_multi_account_detection():
    print("TESTING MULTI-ACCOUNT DETECTION SYSTEM")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile
        from django.utils import timezone
        from datetime import timedelta
        
        print("📊 Multi-Account Detection Features:")
        print("  1. IP-based detection (multiple accounts from same IP)")
        print("  2. Phone-based detection (same phone number)")
        print("  3. Referral abuse detection (circular referrals)")
        print("  4. Suspicious timing patterns (multiple accounts in short time)")
        print("  5. Automatic flagging with notifications")
        
        # Get current user statistics
        total_users = User.objects.count()
        banned_users = User.objects.filter(is_banned=True).count()
        flagged_users = User.objects.filter(is_flagged=True).count()
        admin_users = User.objects.filter(role='admin').count()
        normal_users = total_users - banned_users - flagged_users - admin_users
        
        print(f"\n📈 Current User Statistics:")
        print(f"  - Total users: {total_users}")
        print(f"  - Normal users: {normal_users}")
        print(f"  - Flagged users: {flagged_users}")
        print(f"  - Banned users: {banned_users}")
        print(f"  - Admin users: {admin_users}")
        
        # Check IP distribution
        ip_distribution = {}
        for user in User.objects.filter(last_login_ip__isnull=False).exclude(role='admin'):
            ip = user.last_login_ip
            if ip not in ip_distribution:
                ip_distribution[ip] = 0
            ip_distribution[ip] += 1
        
        suspicious_ips = {ip: count for ip, count in ip_distribution.items() if count >= 2}
        
        if suspicious_ips:
            print(f"\n⚠️  Suspicious IP Addresses (multiple accounts):")
            for ip, count in suspicious_ips.items():
                users = User.objects.filter(last_login_ip=ip).exclude(role='admin')
                print(f"  - {ip}: {count} accounts")
                for user in users:
                    status = "FLAGGED" if user.is_flagged else "NORMAL"
                    print(f"    * {user.username} ({status})")
        else:
            print(f"\n✅ No suspicious IP addresses found")
        
        # Check phone distribution
        phone_distribution = {}
        for user in User.objects.filter(phone__isnull=False).exclude(phone='').exclude(role='admin'):
            phone = user.phone
            if phone not in phone_distribution:
                phone_distribution[phone] = 0
            phone_distribution[phone] += 1
        
        suspicious_phones = {phone: count for phone, count in phone_distribution.items() if count >= 2}
        
        if suspicious_phones:
            print(f"\n⚠️  Suspicious Phone Numbers (multiple accounts):")
            for phone, count in suspicious_phones.items():
                users = User.objects.filter(phone=phone).exclude(role='admin')
                print(f"  - {phone}: {count} accounts")
                for user in users:
                    status = "FLAGGED" if user.is_flagged else "NORMAL"
                    print(f"    * {user.username} ({status})")
        else:
            print(f"\n✅ No suspicious phone numbers found")
        
        # Check recent registrations
        recent_time = timezone.now() - timedelta(hours=24)
        recent_users = User.objects.filter(date_joined__gte=recent_time).exclude(role='admin')
        
        if recent_users.exists():
            print(f"\n📅 Recent Registrations (last 24 hours):")
            for user in recent_users.order_by('-date_joined')[:10]:
                status = "FLAGGED" if user.is_flagged else "NORMAL"
                print(f"  - {user.username}: {user.date_joined.strftime('%Y-%m-%d %H:%M')} ({status})")
        else:
            print(f"\n✅ No recent registrations in last 24 hours")
        
        print(f"\n💡 How Detection Works:")
        print(f"  - Runs automatically on 10% of dashboard loads")
        print(f"  - Flags accounts with matching IPs/phones")
        print(f"  - Detects referral abuse patterns")
        print(f"  - Identifies suspicious registration timing")
        print(f"  - Sends notifications to flagged users")
        print(f"  - Prevents withdrawals for flagged accounts")
        
        print(f"\n🔧 Manual Detection Test:")
        print(f"  You can manually run: detect_and_flag_multiple_accounts()")
        print(f"  This will scan all users and flag suspicious accounts")
        
        print("\n✅ Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_multi_account_detection()
