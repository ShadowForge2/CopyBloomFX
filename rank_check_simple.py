import os
import sys
sys.path.insert(0, os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

import django
django.setup()
from crypto.models import Deposit, Profile, Rank, Notification
from django.contrib.auth import get_user_model
from decimal import Decimal

User = get_user_model()
print('CHECKING RANK CHANGES DUE TO EXPIRED DEPOSITS')
print('=' * 60)

# Get ranks
ranks = Rank.objects.order_by('min_balance')
print('Available Ranks:')
for rank in ranks:
    print(f'  {rank.name}: ${rank.min_balance}+')

# Users with expired deposits
expired_deposits = Deposit.objects.filter(status='expired')
users_with_expired = set(expired_deposits.values_list('user', flat=True))

print(f'\nUsers with expired deposits: {len(users_with_expired)}')
print('-' * 40)

rank_mismatches = 0
correct_ranks = 0

for user_id in users_with_expired:
    user = User.objects.get(id=user_id)
    profile = user.profile
    current_rank = profile.rank
    
    # Calculate expected rank
    expected_rank = None
    for rank in ranks:
        if profile.locked_balance >= rank.min_balance:
            expected_rank = rank
    
    user_expired = expired_deposits.filter(user=user)
    total_expired = sum(d.amount for d in user_expired)
    
    print(f'\nUser: {user.username}')
    print(f'  Current Rank: {current_rank.name if current_rank else "None"}')
    print(f'  Expected Rank: {expected_rank.name if expected_rank else "None"}')
    print(f'  Locked Balance: ${profile.locked_balance}')
    print(f'  Expired Amount: ${total_expired}')
    
    if current_rank != expected_rank:
        print(f'  *** RANK MISMATCH! ***')
        rank_mismatches += 1
    else:
        print(f'  *** Rank is CORRECT ***')
        correct_ranks += 1

print(f'\nSUMMARY:')
print(f'  Users with correct ranks: {correct_ranks}')
print(f'  Users with rank mismatches: {rank_mismatches}')

# Run expired deposit processing again
print('\nRunning expired deposit processing...')
from crypto.views import process_expired_deposits
process_expired_deposits()
print('Processing completed.')
