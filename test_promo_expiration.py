"""
Test script to verify promo code expiration system
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_promo_expiration():
    print("TESTING PROMO CODE EXPIRATION SYSTEM")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Deposit, PromoCode, PromoRedemption
        from django.utils import timezone
        from datetime import timedelta
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Check user's deposits (including promo deposits)
        deposits = Deposit.objects.filter(user=test_user).order_by('-created_at')
        print(f"\n📋 User Deposits (including promos):")
        
        promo_deposits = []
        regular_deposits = []
        
        for deposit in deposits:
            if deposit.network == 'PROMO':
                promo_deposits.append(deposit)
                time_until_expiry = deposit.expires_at - timezone.now()
                days_left = time_until_expiry.days
                hours_left = time_until_expiry.seconds // 3600
                
                status_emoji = "✅" if days_left > 0 else "❌"
                print(f"  {status_emoji} PROMO: ${deposit.amount} - expires in {days_left}d {hours_left}h")
                print(f"     Created: {deposit.created_at.strftime('%Y-%m-%d %H:%M')}")
                print(f"     Expires: {deposit.expires_at.strftime('%Y-%m-%d %H:%M')}")
            else:
                regular_deposits.append(deposit)
        
        # Show regular deposits
        if regular_deposits:
            print(f"\n💰 Regular Deposits:")
            for deposit in regular_deposits[:5]:  # Show first 5
                time_until_expiry = deposit.expires_at - timezone.now()
                if deposit.expires_at:
                    days_left = time_until_expiry.days
                    status_emoji = "✅" if days_left > 0 else "❌"
                    print(f"  {status_emoji} ${deposit.amount} ({deposit.network}) - {days_left}d left")
                else:
                    print(f"  ❓ ${deposit.amount} ({deposit.network}) - no expiry")
        
        # Show available promo codes
        print(f"\n🎫 Available Promo Codes:")
        promos = PromoCode.objects.filter(status='active')
        for promo in promos:
            print(f"  - {promo.code}: ${promo.bonus_min}-${promo.bonus_max} bonus")
            if promo.expiration:
                days_until_expire = (promo.expiration - timezone.now()).days
                print(f"    Code expires in: {days_until_expire} days")
            else:
                print(f"    Code never expires")
            if promo.usage_limit:
                remaining = promo.usage_limit - (promo.usage_count or 0)
                print(f"    Uses remaining: {remaining}")
        
        # Check user's promo redemptions
        redemptions = PromoRedemption.objects.filter(user=test_user).order_by('-created_at')
        if redemptions.exists():
            print(f"\n🏆 User's Promo Redemptions:")
            for redemption in redemptions:
                print(f"  - {redemption.promo_code.code}: ${redemption.bonus_amount:.2f} on {redemption.created_at.strftime('%Y-%m-%d')}")
        
        print(f"\n💡 How Promo Expiration Works:")
        print(f"  1. User redeems promo code")
        print(f"  2. Deposit entry created with 'PROMO' network")
        print(f"  3. 30-day expiration timer starts")
        print(f"  4. Expired promos removed from locked balance")
        print(f"  5. Rank may demote if balance drops")
        
        print(f"\n🎯 FIFO Order for Expiration:")
        print(f"  - Oldest deposits expire first (regular + promo)")
        print(f"  - Promo deposits treated same as regular deposits")
        print(f"  - All follow same 30-day expiration rules")
        
        print("\n✅ Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_promo_expiration()
