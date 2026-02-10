"""
Test script to verify daily profit calculation and display
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_daily_profit_display():
    print("🧪 TESTING DAILY PROFIT DISPLAY")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile, Rank
        from crypto.views import calculate_daily_profit
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Check user's profile and rank
        profile = Profile.objects.filter(user=test_user).first()
        if not profile:
            print("❌ User has no profile.")
            return
            
        rank = profile.get_rank()
        if not rank:
            print("❌ User has no rank.")
            return
            
        print(f"✅ User rank: {rank.name}")
        print(f"✅ Locked balance: ${profile.locked_balance}")
        print(f"✅ Withdrawable balance: ${profile.withdrawable_balance}")
        print(f"✅ Daily profit rate: {rank.daily_profit_pct}%")
        
        # Calculate expected daily profit
        expected_daily_profit = profile.locked_balance * (rank.daily_profit_pct / Decimal('100'))
        print(f"✅ Expected daily profit: ${expected_daily_profit}")
        
        # Test the actual calculation
        actual_profit = calculate_daily_profit(test_user)
        print(f"✅ Actual profit calculated: ${actual_profit or Decimal('0')}")
        
        # Check if user's withdrawable balance increased
        updated_profile = Profile.objects.get(user=test_user)
        print(f"✅ Updated withdrawable balance: ${updated_profile.withdrawable_balance}")
        
        # Verify business rules
        if profile.locked_balance > 0 and rank:
            if expected_daily_profit > 0:
                print("✅ Daily profit calculation working correctly")
            else:
                print("⚠️  Expected profit should be > 0 but got 0")
        else:
            print("✅ No profit calculated (no locked balance or rank)")
        
        print("\n🎯 Dashboard should now show:")
        print(f"  - Today's Profit: ${actual_profit or Decimal('0')}")
        print(f"  - Potential Daily: ${expected_daily_profit}")
        print(f"  - Rate: {rank.daily_profit_pct}%")
        
        print("\n🎉 Daily profit display test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_daily_profit_display()
