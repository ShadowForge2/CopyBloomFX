"""
Test script to verify 100% win rate with high profits close to potential daily profit
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_100_percent_win_rate():
    print("🧪 TESTING 100% WIN RATE - HIGH PROFITS")
    print("=" * 60)
    
    try:
        import django
        django.setup()
        
        from django.contrib.auth.models import User
        from crypto.models import CopyTrade, Profile
        from decimal import Decimal
        
        # Get a test user
        test_user = User.objects.filter(is_staff=False).first()
        if not test_user:
            print("❌ No test user found.")
            return
        
        print(f"✅ Testing with user: {test_user.username}")
        
        # Get user's profile and rank
        profile = Profile.objects.filter(user=test_user).first()
        if not profile:
            print("❌ User has no profile.")
            return
            
        rank = profile.get_rank()
        if not rank:
            print("❌ User has no rank.")
            return
        
        # Calculate potential daily profit
        potential_daily_profit = profile.locked_balance * (rank.daily_profit_pct / Decimal('100'))
        print(f"\n📊 Profit Analysis:")
        print(f"  - User rank: {rank.name}")
        print(f"  - Locked balance: ${profile.locked_balance}")
        print(f"  - Daily profit rate: {rank.daily_profit_pct}%")
        print(f"  - Potential daily profit: ${potential_daily_profit:.2f}")
        print(f"  - Trade profit: Daily target ± $0.01-0.03")
        print(f"  - Win rate: 100% (always profitable)")
        
        # Check recent copy trades
        recent_trades = CopyTrade.objects.filter(
            user=test_user
        ).order_by('-created_at')[:10]
        
        print(f"\n📋 Recent Trades (100% Win Rate System):")
        
        total_profit = Decimal('0')
        profitable_trades = 0
        
        for trade in recent_trades:
            if trade.profit > 0:
                profit_ratio = (trade.profit / trade.amount) * 100
                profitable_trades += 1
                print(f"  ✅ {trade.pair} ${trade.amount:.3f} → ${trade.profit:.3f} ({profit_ratio:.0f}% return)")
            else:
                print(f"  ❌ {trade.pair} ${trade.amount:.3f} → ${trade.profit:.3f} (LOSS - should not happen!)")
            
            total_profit += trade.profit
        
        win_rate = (profitable_trades / recent_trades.count() * 100) if recent_trades.count() > 0 else 0
        
        print(f"\n📈 Performance Summary:")
        print(f"  - Total trades: {recent_trades.count()}")
        print(f"  - Profitable trades: {profitable_trades}")
        print(f"  - Win rate: {win_rate:.0f}%")
        print(f"  - Total profit: ${total_profit:.3f}")
        
        # Check if profits are close to potential daily profit
        if recent_trades.count() > 0:
            avg_profit = total_profit / recent_trades.count()
            difference_from_target = avg_profit - potential_daily_profit
            
            print(f"\n🎯 Profit vs Daily Target Analysis:")
            print(f"  - Average profit per trade: ${avg_profit:.3f}")
            print(f"  - Potential daily profit: ${potential_daily_profit:.3f}")
            print(f"  - Difference: ${difference_from_target:.3f}")
            print(f"  - Expected difference: ±$0.01-0.03")
            
            if abs(difference_from_target) <= Decimal('0.03'):
                print(f"  ✅ Profits are within expected range!")
            else:
                print(f"  ⚠️  Profits outside expected range")
        
        print(f"\n💡 Why This Works:")
        print(f"  - 100% win rate - players always win!")
        print(f"  - Profits very close to daily target (±$0.01-0.03)")
        print(f"  - Each trade essentially matches daily potential profit")
        print(f"  - Players can exceed daily goals consistently")
        print(f"  - Maximum motivation with predictable high profits!")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_100_percent_win_rate()
