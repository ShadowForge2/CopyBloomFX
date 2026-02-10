"""
Test script to demonstrate realistic delayed copy trading system
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def test_realistic_trading():
    print("🧪 TESTING REALISTIC DELAYED COPY TRADING")
    print("=" * 60)
    
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
        
        print(f"\n📊 Realistic Trading System:")
        print(f"  - Trade submission: Immediate (status: pending)")
        print(f"  - 0-10 seconds: $0.00 profit (processing)")
        print(f"  - 10-30 seconds: Gradual profit increase (fluctuating)")
        print(f"  - 30-35 seconds: Full profit achieved")
        print(f"  - 35+ seconds: Trade completed, profit added to balance")
        
        # Check recent copy trades
        recent_trades = CopyTrade.objects.filter(
            user=test_user
        ).order_by('-created_at')[:10]
        
        print(f"\n📋 Recent Trades (Realistic System):")
        
        for trade in recent_trades:
            time_elapsed = timezone.now() - trade.created_at
            seconds_elapsed = time_elapsed.total_seconds()
            
            # Determine trade stage
            if seconds_elapsed < 10:
                stage = "Processing"
                emoji = "⏳"
            elif seconds_elapsed < 30:
                stage = "Active"
                emoji = "📈"
            elif seconds_elapsed < 35:
                stage = "Completing"
                emoji = "✅"
            else:
                stage = "Completed"
                emoji = "💰"
            
            print(f"  {emoji} {trade.pair} {trade.action}: ${trade.amount:.3f} → ${trade.profit:.3f} ({stage}, {seconds_elapsed:.0f}s ago)")
        
        # Show pending trades specifically
        pending_trades = CopyTrade.objects.filter(user=test_user, status='pending')
        if pending_trades.exists():
            print(f"\n🔄 Pending Trades ({pending_trades.count()}):")
            for trade in pending_trades:
                time_elapsed = timezone.now() - trade.created_at
                seconds_elapsed = time_elapsed.total_seconds()
                
                if seconds_elapsed < 10:
                    status = "Initializing..."
                elif seconds_elapsed < 30:
                    progress = (seconds_elapsed - 10) / 20 * 100  # 10-30s progress
                    status = f"In progress ({progress:.0f}%)"
                else:
                    status = "Finalizing..."
                
                print(f"  - {trade.pair}: ${trade.profit:.3f} ({status})")
        
        print(f"\n💡 Why This Works:")
        print(f"  - Realistic delay: Trades don't complete instantly")
        print(f"  - Fluctuating profits: Simulates real market movement")
        print(f"  - Gradual progress: Profit builds over time")
        print(f"  - Authentic experience: Feels like real trading")
        print(f"  - Anticipation: Users watch profits grow")
        
        print(f"\n🎯 User Experience:")
        print(f"  1. Submit trade → 'Processing...' (0-10s)")
        print(f"  2. Watch profit → See gradual increase (10-30s)")
        print(f"  3. Trade completes → Profit added to balance (35s+)")
        print(f"  4. Refresh page → See updated profits in real-time")
        
        print("\n🎉 Test completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_realistic_trading()
