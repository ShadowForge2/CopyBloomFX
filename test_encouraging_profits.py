"""
Test script to verify the new more encouraging copy trade profit ranges
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_encouraging_profits():
    print("🧪 TESTING NEW ENCOURAGING COPY TRADE PROFITS")
    print("=" * 60)
    
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
        
        print(f"\n📊 New Copy Trade Profit Analysis:")
        print(f"  - Win Rate: 90% (very encouraging!)")
        print(f"  - Profit Range: 20% to 200% return")
        print(f"  - Loss Range: 5% to 50% loss")
        print(f"  - Lot Size: $0.01 to $0.10")
        
        print(f"\n📋 Recent Trades (New Encouraging System):")
        
        total_profit = Decimal('0')
        profitable_trades = 0
        loss_trades = 0
        
        for trade in recent_trades:
            if trade.profit > 0:
                profit_ratio = (trade.profit / trade.amount) * 100
                profitable_trades += 1
                print(f"  ✅ {trade.pair} ${trade.amount:.3f} → ${trade.profit:.3f} ({profit_ratio:.0f}% return)")
            else:
                loss_ratio = (abs(trade.profit) / trade.amount) * 100
                loss_trades += 1
                print(f"  ❌ {trade.pair} ${trade.amount:.3f} → ${trade.profit:.3f} ({loss_ratio:.0f}% loss)")
            
            total_profit += trade.profit
        
        win_rate = (profitable_trades / recent_trades.count() * 100) if recent_trades.count() > 0 else 0
        
        print(f"\n📈 Performance Summary:")
        print(f"  - Total trades: {recent_trades.count()}")
        print(f"  - Profitable trades: {profitable_trades}")
        print(f"  - Loss trades: {loss_trades}")
        print(f"  - Win rate: {win_rate:.0f}%")
        print(f"  - Total profit: ${total_profit:.3f}")
        
        # Show expected ranges
        print(f"\n🎯 Expected Profit Examples:")
        print(f"  - Lot $0.01 → Profit $0.002 to $0.02 (20%-200%)")
        print(f"  - Lot $0.05 → Profit $0.01 to $0.10 (20%-200%)")
        print(f"  - Lot $0.10 → Profit $0.02 to $0.20 (20%-200%)")
        
        print(f"\n💡 Why This Works:")
        print(f"  - 90% win rate highly encourages players")
        print(f"  - Small lots keep risk low")
        print(f"  - Good returns make it attractive")
        print(f"  - Still reasonable compared to daily limits")
        print(f"  - Builds player confidence quickly")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_encouraging_profits()
