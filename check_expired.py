import os
import sys
sys.path.insert(0, os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

import django
django.setup()
from crypto.models import Deposit, Profile, Rank
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()
print('CHECKING EXPIRED DEPOSITS AFTER ONE MONTH')
print('=' * 50)

# Check all deposits
deposits = Deposit.objects.all().order_by('-created_at')
print(f'Total deposits: {deposits.count()}')

expired_count = 0
expiring_soon_count = 0

for deposit in deposits:
    if deposit.expires_at:
        time_until_expiry = deposit.expires_at - timezone.now()
        days_until_expiry = time_until_expiry.days
        
        if days_until_expiry <= 0:
            expired_count += 1
            print(f'EXPIRED: ${deposit.amount} for {deposit.user.username} - Expired on {deposit.expires_at.strftime("%Y-%m-%d")}')
        elif days_until_expiry <= 7:
            expiring_soon_count += 1
            print(f'EXPIRING SOON: ${deposit.amount} for {deposit.user.username} - {days_until_expiry} days left')

print(f'\nSummary:')
print(f'- Expired deposits: {expired_count}')
print(f'- Expiring within 7 days: {expiring_soon_count}')

# Check if expiration processing is working
print('\nPROCESSING EXPIRED DEPOSITS...')
from crypto.views import process_expired_deposits
process_expired_deposits()
print('Expired deposit processing completed.')
