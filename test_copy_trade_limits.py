"""
Test script to verify copy trade limits are working correctly
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_copy_trade_limits():
    print("🧪 TESTING COPY TRADE LIMITS")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile, Rank, CopyTrade
        from crypto.views import get_concurrent_copy_trades
        
        # Get a test user (or create one)
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found. Please create a user first.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Check user's rank
        profile = Profile.objects.filter(user=test_user).first()
        if not profile:
            print("❌ User has no profile.")
            return
            
        rank = profile.get_rank()
        if not rank:
            print("❌ User has no rank.")
            return
            
        print(f"✅ User rank: {rank.name}")
        print(f"✅ Max trades allowed: {rank.copy_trades_limit} per 24 hours")
        
        # Check current trades in last 24 hours
        current_trades = get_concurrent_copy_trades(test_user)
        print(f"✅ Current trades in last 24h: {current_trades}")
        
        # Show recent trades
        recent_trades = CopyTrade.objects.filter(
            user=test_user
        ).order_by('-created_at')[:5]
        
        print(f"\n📋 Recent trades for {test_user.username}:")
        for trade in recent_trades:
            print(f"  - {trade.created_at.strftime('%Y-%m-%d %H:%M')}: {trade.pair} {trade.action} ${trade.amount} (Profit: ${trade.profit})")
        
        # Verify profit is always 0
        non_zero_profits = CopyTrade.objects.filter(user=test_user, profit__gt=0).count()
        if non_zero_profits > 0:
            print(f"⚠️  WARNING: Found {non_zero_profits} trades with non-zero profit!")
        else:
            print("✅ All copy trades have profit = 0 (correct)")
        
        print(f"\n🎯 Copy trade limit status: {current_trades}/{rank.copy_trades_limit}")
        
        if current_trades >= rank.copy_trades_limit:
            print("🚫 User has reached their copy trade limit for today")
        else:
            print("✅ User can still execute more copy trades")
            
        print("\n🎉 Copy trade limit test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_copy_trade_limits()
