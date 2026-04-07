import os
import sys
sys.path.insert(0, os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

import django
django.setup()
from crypto.models import Deposit, Profile, Rank, Notification
from django.contrib.auth import get_user_model
from django.utils import timezone
from decimal import Decimal

User = get_user_model()
print('CHECKING RANK CHANGES DUE TO EXPIRED DEPOSITS')
print('=' * 60)

# Get all ranks for reference
ranks = Rank.objects.order_by('min_balance')
print('Available Ranks:')
for rank in ranks:
    print(f'  {rank.name}: ${rank.min_balance}+ ({rank.daily_profit_pct}% daily)')

print('\n' + '=' * 60)
print('USER RANK ANALYSIS:')

# Check users with expired deposits
users_with_expired = set()
expired_deposits = Deposit.objects.filter(status='expired')
for deposit in expired_deposits:
    users_with_expired.add(deposit.user)

print(f'Users with expired deposits: {len(users_with_expired)}')

for user in users_with_expired:
    profile = user.profile
    current_rank = profile.rank
    
    # Calculate what the rank should be based on current locked balance
    expected_rank = None
    for rank in ranks:
        if profile.locked_balance >= rank.min_balance:
            expected_rank = rank
    
    # Get user's expired deposits
    user_expired_deposits = expired_deposits.filter(user=user)
    total_expired_amount = sum(d.amount for d in user_expired_deposits)
    
    print(f'\n👤 {user.username}:')
    print(f'  Current Rank: {current_rank.name if current_rank else "None"}')
    print(f'  Expected Rank: {expected_rank.name if expected_rank else "None"}')
    print(f'  Locked Balance: ${profile.locked_balance}')
    print(f'  Withdrawable Balance: ${profile.withdrawable_balance}')
    print(f'  Total Balance: ${profile.principal_balance}')
    print(f'  Expired Deposits: {user_expired_deposits.count()} (${total_expired_amount})')
    
    # Check if ranks match
    if current_rank != expected_rank:
        print(f'  ⚠️  RANK MISMATCH! Current ≠ Expected')
    else:
        print(f'  ✅ Rank is correct')
    
    # Check for rank change notifications
    rank_notifications = Notification.objects.filter(
        user=user,
        message__contains='rank'
    ).order_by('-created_at')[:5]
    
    if rank_notifications.exists():
        print(f'  📧 Rank Notifications ({rank_notifications.count()}):')
        for notif in rank_notifications:
            print(f'    - {notif.created_at.strftime("%Y-%m-%d")}: {notif.message[:50]}...')
    else:
        print(f'  📧 No rank notifications found')

print('\n' + '=' * 60)
print('PROCESSING EXPIRED DEPOSITS AGAIN TO VERIFY...')
from crypto.views import process_expired_deposits
process_expired_deposits()
print('✅ Expired deposit processing completed')
