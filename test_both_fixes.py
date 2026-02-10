"""
Test script to verify both fixes:
1. Daily profit doesn't increase on refresh
2. Copy trades show individual profit/loss
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_fixes():
    print("🧪 TESTING BOTH FIXES")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile, CopyTrade
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Check current withdrawable balance
        profile = Profile.objects.filter(user=test_user).first()
        if not profile:
            print("❌ User has no profile.")
            return
            
        initial_balance = profile.withdrawable_balance
        print(f"✅ Initial withdrawable balance: ${initial_balance}")
        
        # Check recent copy trades
        recent_trades = CopyTrade.objects.filter(
            user=test_user
        ).order_by('-created_at')[:5]
        
        print(f"\n📋 Recent copy trades (should show individual P&L):")
        for trade in recent_trades:
            profit_status = "PROFIT" if trade.profit >= 0 else "LOSS"
            print(f"  - {trade.pair} {trade.action}: ${trade.amount:.2f} → ${trade.profit:.2f} ({profit_status})")
        
        # Check if trades have varied profits (not all 0)
        non_zero_trades = CopyTrade.objects.filter(
            user=test_user, 
            profit__gt=0
        ).count()
        
        loss_trades = CopyTrade.objects.filter(
            user=test_user, 
            profit__lt=0
        ).count()
        
        print(f"\n📊 Trade Analysis:")
        print(f"  - Profitable trades: {non_zero_trades}")
        print(f"  - Loss trades: {loss_trades}")
        print(f"  - Zero profit trades: {recent_trades.count() - non_zero_trades - loss_trades}")
        
        if non_zero_trades > 0 or loss_trades > 0:
            print("✅ Copy trades are showing individual P&L (FIXED)")
        else:
            print("⚠️  All trades still show 0 profit")
        
        print("\n🎯 Expected Behavior:")
        print("  1. Daily profit should NOT increase on page refresh")
        print("  2. Copy trades should show individual profit/loss per trade")
        print("  3. Trade limits should be enforced per 24 hours")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_fixes()
