"""
Manual SQL to update daily profit rates to 3.67% for all ranks
Run this in Django shell: python manage.py shell
"""

# Copy and paste these commands into Django shell

from crypto.models import Rank
from decimal import Decimal

# Update all ranks to have 3.67% daily profit rate
new_rate = Decimal('3.67')
ranks_updated = Rank.objects.all().update(daily_profit_pct=new_rate)

print(f"Updated {ranks_updated} ranks to {new_rate}% daily profit rate")

# Show the updated ranks
for rank in Rank.objects.all().order_by('min_balance'):
    daily_profit = rank.min_balance * (new_rate / 100)
    monthly_profit = daily_profit * 30
    total_return = rank.min_balance + monthly_profit
    return_pct = (total_return / rank.min_balance - 1) * 100
    
    print(f"{rank.name}: ${rank.min_balance} → ${total_return:.2f} ({return_pct:.1f}% return in 30 days)")

print("\nCalculation: 3.67% daily × 30 days = 110.1% total return")
print("This ensures users make locked_balance + 10.1% profit before deposits expire")
