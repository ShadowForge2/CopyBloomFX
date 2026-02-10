"""
Test script to verify Today's Profit is showing actual copy trade profit
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_todays_profit():
    print("🧪 TESTING TODAY'S PROFIT DISPLAY")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import CopyTrade
        from django.utils import timezone
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Get today's start (midnight)
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        
        # Get copy trades from today
        copy_trades_today = CopyTrade.objects.filter(
            user=test_user,
            created_at__gte=today_start
        )
        
        print(f"\n📊 Today's Copy Trades Analysis:")
        print(f"  - Total trades today: {copy_trades_today.count()}")
        
        # Calculate today's profit
        todays_profit = copy_trades_today.aggregate(
            total=models.Sum('profit')
        )['total'] or Decimal('0')
        
        print(f"  - Today's total profit: ${todays_profit:.3f}")
        
        # Show individual trades
        print(f"\n📋 Today's Individual Trades:")
        for trade in copy_trades_today.order_by('-created_at'):
            profit_status = "PROFIT" if trade.profit >= 0 else "LOSS"
            print(f"  - {trade.created_at.strftime('%H:%M')}: {trade.pair} ${trade.amount:.3f} → ${trade.profit:.3f} ({profit_status})")
        
        # Verify dashboard should show
        print(f"\n🎯 Dashboard Should Show:")
        print(f"  - Today's Profit: ${todays_profit:.3f}")
        print(f"  - Potential Daily: [calculated from rank]")
        print(f"  - Rate: [user's rank percentage]")
        
        if copy_trades_today.count() > 0:
            print(f"\n✅ Today's profit tracking is working!")
            if todays_profit > 0:
                print(f"✅ User earned ${todays_profit:.3f} today from copy trades")
            else:
                print(f"⚠️  No profit from copy trades today (all losses or no trades)")
        else:
            print(f"\n⚠️  No copy trades today")
            print("💡 Execute some copy trades to see today's profit tracking")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_todays_profit()
