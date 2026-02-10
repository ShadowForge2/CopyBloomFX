"""
Test script to verify small lot sizes generate big profits
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_small_lots_big_profits():
    print("🧪 TESTING SMALL LOTS - BIG PROFITS")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import CopyTrade
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Check recent copy trades
        recent_trades = CopyTrade.objects.filter(
            user=test_user
        ).order_by('-created_at')[:10]
        
        print(f"\n📋 Recent copy trades (Small Lots - Big Profits):")
        
        small_lot_count = 0
        big_profit_count = 0
        
        for trade in recent_trades:
            # Check if lot size is small (0.01 to 0.1)
            is_small_lot = Decimal('0.01') <= trade.amount <= Decimal('0.1')
            if is_small_lot:
                small_lot_count += 1
            
            # Check if profit is big relative to lot size
            if trade.profit > 0:
                profit_ratio = trade.profit / trade.amount
                is_big_profit = profit_ratio >= Decimal('0.5')  # 50% or more return
                if is_big_profit:
                    big_profit_count += 1
                
                print(f"  - {trade.pair} {trade.action}: Lot ${trade.amount:.3f} → Profit ${trade.profit:.3f} ({profit_ratio:.1f}x return)")
            else:
                print(f"  - {trade.pair} {trade.action}: Lot ${trade.amount:.3f} → Loss ${abs(trade.profit):.3f}")
        
        print(f"\n📊 Analysis:")
        print(f"  - Total trades checked: {recent_trades.count()}")
        print(f"  - Small lot trades (0.01-0.1): {small_lot_count}")
        print(f"  - Big profit trades (50%+ return): {big_profit_count}")
        
        # Verify lot sizes are in correct range
        if small_lot_count == recent_trades.count():
            print("✅ All trades use small lot sizes (0.01-0.1)")
        else:
            print("⚠️  Some trades are not using small lot sizes")
        
        # Verify profit potential
        profitable_trades = recent_trades.filter(profit__gt=0)
        if profitable_trades.exists():
            avg_profit_ratio = sum(trade.profit / trade.amount for trade in profitable_trades) / profitable_trades.count()
            print(f"✅ Average profit return: {avg_profit_ratio:.1f}x")
            
            if avg_profit_ratio >= Decimal('0.5'):
                print("✅ Small lots are generating big profits!")
            else:
                print("⚠️  Profit returns could be higher")
        
        print("\n🎯 Expected Behavior:")
        print("  - Lot sizes: $0.01 to $0.10 (very small)")
        print("  - Profit returns: 50% to 500% (big profits)")
        print("  - Losses: 10% to 90% of small lot")
        print("  - Shows power of copy trading: small lots → big profits")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_small_lots_big_profits()
