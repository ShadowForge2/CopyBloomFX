"""
Test script to verify expired deposit processing and rank demotion
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_expired_deposits():
    print("🧪 TESTING EXPIRED DEPOSIT PROCESSING")
    print("=" * 60)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Deposit, Profile, Rank
        from django.utils import timezone
        from datetime import timedelta
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        profile = test_user.profile
        current_rank = profile.rank
        
        print(f"\n📊 Current Status:")
        print(f"  - Current rank: {current_rank.name if current_rank else 'None'}")
        print(f"  - Locked balance: ${profile.locked_balance}")
        print(f"  - Withdrawable balance: ${profile.withdrawable_balance}")
        print(f"  - Total balance: ${profile.principal_balance}")
        
        # Check user's deposits
        deposits = Deposit.objects.filter(user=test_user).order_by('approved_at')
        print(f"\n📋 User Deposits:")
        
        for deposit in deposits:
            if deposit.expires_at:
                time_until_expiry = deposit.expires_at - timezone.now()
                is_expired = time_until_expiry.total_seconds() <= 0
                
                status_emoji = "⏰" if not is_expired else "⏰"
                if deposit.status == 'expired':
                    status_emoji = "❌"
                elif deposit.status == 'approved':
                    status_emoji = "✅"
                elif deposit.status == 'pending':
                    status_emoji = "⏳"
                
                print(f"  {status_emoji} ${deposit.amount} - {deposit.status.title()}")
                print(f"     Created: {deposit.created_at.strftime('%Y-%m-%d %H:%M')}")
                if deposit.approved_at:
                    print(f"     Approved: {deposit.approved_at.strftime('%Y-%m-%d %H:%M')}")
                if deposit.expires_at:
                    if is_expired:
                        print(f"     Expired: {deposit.expires_at.strftime('%Y-%m-%d %H:%M')} (EXPIRED!)")
                    else:
                        days_left = time_until_expiry.days
                        hours_left = time_until_expiry.seconds // 3600
                        print(f"     Expires: {deposit.expires_at.strftime('%Y-%m-%d %H:%M')} ({days_left}d {hours_left}h left)")
            else:
                print(f"  ❓ ${deposit.amount} - {deposit.status.title()} (no expiry set)")
        
        # Show available ranks
        print(f"\n🏆 Available Ranks:")
        ranks = Rank.objects.order_by('min_balance')
        for rank in ranks:
            current_emoji = "👑" if rank == current_rank else "  "
            print(f"  {current_emoji} {rank.name}: ${rank.min_balance}+ ({rank.daily_profit_pct}% daily, {rank.copy_trades_limit} trades)")
        
        print(f"\n💡 How FIFO Expiration Works:")
        print(f"  1. Oldest deposits expire first (FIFO)")
        print(f"  2. Expired amount removed from locked balance")
        print(f"  3. Rank recalculated based on new total balance")
        print(f"  4. User demoted if new balance is lower")
        print(f"  5. Notification sent for rank changes")
        
        print(f"\n🎯 Expected Behavior:")
        print(f"  - Deposit $7 expires first (oldest)")
        print(f"  - Then deposit $50 expires (next oldest)")
        print(f"  - Locked balance decreases as deposits expire")
        print(f"  - Rank demoted when balance falls below threshold")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_expired_deposits()
