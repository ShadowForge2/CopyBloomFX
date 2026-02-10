from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from crypto.models import Rank, Profile

User = get_user_model()

RANKS = [
    {'name': 'Green Horn', 'min_balance': 7, 'max_balance': 49, 'daily_profit_percentage': 1.67, 'max_copy_trades': 1, 'color': '#4CAF50'},
    {'name': 'Student Form', 'min_balance': 50, 'max_balance': 100, 'daily_profit_percentage': 2.0, 'max_copy_trades': 2, 'color': '#2196F3'},
    {'name': 'Market Maven', 'min_balance': 100, 'max_balance': 500, 'daily_profit_percentage': 2.0, 'max_copy_trades': 3, 'color': '#9C27B0'},
    {'name': 'Gunslinger', 'min_balance': 500, 'max_balance': 1500, 'daily_profit_percentage': 2.2, 'max_copy_trades': 4, 'color': '#FF9800'},
    {'name': 'Whale', 'min_balance': 1500, 'max_balance': 5000, 'daily_profit_percentage': 2.5, 'max_copy_trades': 5, 'color': '#FFC107'},
    {'name': 'Market Wizard', 'min_balance': 5000, 'max_balance': None, 'daily_profit_percentage': 2.7, 'max_copy_trades': 6, 'color': '#FFD700'},
]


class Command(BaseCommand):
    help = 'Seed ranks and admin user'

    def handle(self, *args, **options):
        Rank.objects.all().delete()
        for r in RANKS:
            Rank.objects.create(**r)
        self.stdout.write('Seeded ranks.')
        if User.objects.filter(username='admin').exists():
            self.stdout.write('Admin already exists (admin / admin123).')
            return
        admin = User.objects.create_superuser('admin', 'admin@copytrade.local', 'admin123')
        admin.role = 'admin'
        admin.save()
        Profile.objects.create(user=admin, referral_code='ADMIN1')
        self.stdout.write(self.style.SUCCESS('Admin created: username=admin, password=admin123'))
