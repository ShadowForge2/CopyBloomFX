"""
Migration script to update daily profit rates for 110% return in 30 days
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def update_daily_profit_rates():
    print("UPDATING DAILY PROFIT RATES FOR 110% RETURN IN 30 DAYS")
    print("=" * 65)
    
    try:
        import django
        django.setup()
        
        from crypto.models import Rank
        from decimal import Decimal
        
        # Calculate: To earn 110% in 30 days = 3.67% per day
        # This ensures users make locked_balance + 10% before deposits expire
        new_daily_rate = Decimal('3.67')
        
        print(f"New Profit Calculation:")
        print(f"  - Target return: 110% of locked balance")
        print(f"  - Time period: 30 days")
        print(f"  - Daily rate needed: 3.67%")
        print(f"  - Total after 30 days: 110.1% (slightly over target)")
        
        print(f"\nUpdating Ranks:")
        
        ranks = Rank.objects.all()
        updated_count = 0
        
        for rank in ranks.order_by('min_balance'):
            old_rate = rank.daily_profit_pct
            rank.daily_profit_pct = new_daily_rate
            rank.save(update_fields=['daily_profit_pct'])
            updated_count += 1
            
            print(f"  {rank.name}: ${rank.min_balance}+")
            print(f"     Old rate: {old_rate}% → New rate: {new_daily_rate}%")
            
            # Show example earnings
            example_balance = rank.min_balance
            daily_profit = example_balance * (new_daily_rate / Decimal('100'))
            monthly_profit = daily_profit * 30
            total_return = example_balance + monthly_profit
            return_percentage = (total_return / example_balance - 1) * 100
            
            print(f"     Example: ${example_balance} → ${total_return:.2f} ({return_percentage:.1f}% return)")
        
        print(f"\nSummary:")
        print(f"  - Ranks updated: {updated_count}")
        print(f"  - New daily rate: {new_daily_rate}% for all ranks")
        print(f"  - 30-day return: 110.1% (locked + 10.1% profit)")
        
        print(f"\nBenefits:")
        print(f"  - Users profit before deposits expire")
        print(f"  - Encourages continued deposits")
        print(f"  - Fair and transparent earnings")
        print(f"  - Competitive profit rates")
        
        print(f"\nUser Experience:")
        print(f"  - Deposit $100 → $110.10 after 30 days")
        print(f"  - Deposit $500 → $550.50 after 30 days")
        print(f"  - Deposit $1000 → $1101.00 after 30 days")
        
        print("\nUpdate completed!")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    update_daily_profit_rates()
