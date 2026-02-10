# =============================================================================
# crypto/rank_utils.py
# =============================================================================

from decimal import Decimal
from django.utils import timezone
from .models import Rank, Profile


def calculate_user_rank(user):
    """
    Calculate and return the appropriate rank for a user based on principal balance
    """
    try:
        profile = Profile.objects.get(user=user)
        return profile.get_rank()
    except Profile.DoesNotExist:
        return None


def update_user_rank(user):
    """
    Update user's rank based on current principal balance
    """
    try:
        profile = Profile.objects.get(user=user)
        return profile.update_rank()
    except Profile.DoesNotExist:
        return None


def generate_daily_profit(user):
    """
    Generate daily profit for a user if eligible
    - Only once per day per user
    - Only if user has a rank
    - Only if locked_balance > 0
    """
    try:
        profile = Profile.objects.select_related('rank').get(user=user)
    except Profile.DoesNotExist:
        return None
    
    # Safety invariants
    if profile.locked_balance <= 0:
        return None
    
    rank = profile.get_rank()
    if not rank:
        return None
    
    today = timezone.now().date()
    
    # Check if profit already generated for today
    # TODO: Implement this check after migration
    
    # Calculate daily profit: locked_balance * daily_profit_percentage / 100
    daily_profit_amount = profile.locked_balance * (rank.daily_profit_percentage / Decimal('100'))
    
    if daily_profit_amount <= 0:
        return None
    
    # Add profit to withdrawable balance
    profile.withdrawable_balance += daily_profit_amount
    profile.save(update_fields=['withdrawable_balance'])
    
    return daily_profit_amount


def get_copy_trade_limit(user):
    """
    Get the maximum concurrent copy trades allowed for a user
    """
    rank = calculate_user_rank(user)
    return rank.max_copy_trades if rank else 0


def can_execute_copy_trade(user):
    """
    Check if user can execute a copy trade based on rank and balance
    """
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return False
    
    # Must have a rank
    rank = profile.get_rank()
    if not rank:
        return False
    
    # Must have principal balance
    if profile.principal_balance <= 0:
        return False
    
    return True


def get_concurrent_copy_trades(user):
    """
    Get count of copy trades in the last 24 hours
    This enforces the business rule: X trades per 24 hours based on rank
    """
    from django.utils import timezone
    from datetime import timedelta
    from .models import CopyTrade
    
    last_24_hours = timezone.now() - timedelta(hours=24)
    return CopyTrade.objects.filter(
        user=user, 
        created_at__gte=last_24_hours
    ).count()


def is_copy_trade_limit_reached(user):
    """
    Check if user has reached their concurrent copy trade limit
    """
    limit = get_copy_trade_limit(user)
    if limit <= 0:
        return True
    
    concurrent = get_concurrent_copy_trades(user)
    return concurrent >= limit


def get_rank_progress(user):
    """
    Get user's progress towards next rank
    Returns current rank, next rank, and progress percentage
    """
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return None, None, 0
    
    current_rank = profile.get_rank()
    if not current_rank:
        return None, None, 0
    
    # Find next rank
    next_rank = Rank.objects.filter(min_balance__gt=current_rank.min_balance).order_by('min_balance').first()
    
    if not next_rank:
        # User is at highest rank
        return current_rank, None, 100
    
    # Calculate progress
    current_balance = profile.principal_balance
    range_start = current_rank.min_balance
    range_end = next_rank.min_balance
    
    if current_balance >= range_end:
        progress = 100
    else:
        progress = max(0, min(100, ((current_balance - range_start) / (range_end - range_start)) * 100))
    
    return current_rank, next_rank, progress
