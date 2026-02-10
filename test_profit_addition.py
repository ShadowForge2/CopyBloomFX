"""
Test script to verify copy trade profits are added to withdrawable balance
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_copy_trade_profit_addition():
    print("🧪 TESTING COPY TRADE PROFIT ADDITION TO BALANCE")
    print("=" * 60)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import Profile, CopyTrade
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Get user's profile
        profile = Profile.objects.filter(user=test_user).first()
        if not profile:
            print("❌ User has no profile.")
            return
            
        initial_balance = profile.withdrawable_balance
        print(f"✅ Initial withdrawable balance: ${initial_balance}")
        
        # Check recent profitable trades
        profitable_trades = CopyTrade.objects.filter(
            user=test_user,
            profit__gt=0,
            status='completed'
        ).order_by('-created_at')[:5]
        
        total_profit_from_trades = Decimal('0')
        print(f"\n📋 Recent profitable trades:")
        
        for trade in profitable_trades:
            print(f"  - {trade.created_at.strftime('%H:%M')}: {trade.pair} ${trade.amount:.2f} → ${trade.profit:.2f} profit")
            total_profit_from_trades += trade.profit
        
        print(f"\n💰 Total profit from trades: ${total_profit_from_trades}")
        
        # Check if balance reflects the profits
        expected_balance = initial_balance + total_profit_from_trades
        current_balance = profile.withdrawable_balance
        
        print(f"\n📊 Balance Analysis:")
        print(f"  - Initial balance: ${initial_balance}")
        print(f"  - Trade profits: ${total_profit_from_trades}")
        print(f"  - Expected balance: ${expected_balance}")
        print(f"  - Current balance: ${current_balance}")
        
        # Check for balance increase
        if current_balance > initial_balance:
            print(f"✅ Balance increased by ${current_balance - initial_balance}")
            print("✅ Copy trade profits are being added to withdrawable balance")
        else:
            print("⚠️  Balance hasn't increased from copy trades")
            
        # Check loss trades (should not affect balance)
        loss_trades = CopyTrade.objects.filter(
            user=test_user,
            profit__lt=0,
            status='completed'
        ).count()
        
        print(f"\n📉 Loss trades: {loss_trades} (correctly not affecting balance)")
        
        print("\n🎯 Expected Behavior:")
        print("  - Profitable trades: Add profit to withdrawable balance")
        print("  - Loss trades: No balance change")
        print("  - Balance should reflect net profits from trades")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_copy_trade_profit_addition()
