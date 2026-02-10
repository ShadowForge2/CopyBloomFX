"""
Fix any copy trades with non-zero profit to enforce business rules
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def fix_copy_trade_profits():
    print("🔧 FIXING COPY TRADE PROFITS")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from crypto.models import CopyTrade
        
        # Find all trades with non-zero profit
        trades_with_profit = CopyTrade.objects.filter(profit__gt=0)
        
        if trades_with_profit.exists():
            print(f"⚠️  Found {trades_with_profit.count()} trades with non-zero profit")
            print("Fixing these to enforce business rules...")
            
            # Set all profits to 0
            updated = trades_with_profit.update(profit=0)
            print(f"✅ Fixed {updated} trades - profit set to 0")
        else:
            print("✅ All copy trades already have profit = 0")
        
        # Verify the fix
        remaining_issues = CopyTrade.objects.filter(profit__gt=0).count()
        if remaining_issues == 0:
            print("✅ All copy trades now comply with business rules (profit = 0)")
        else:
            print(f"❌ Still have {remaining_issues} trades with non-zero profit")
            
        print("\n🎉 Copy trade profit fix completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    fix_copy_trade_profits()
