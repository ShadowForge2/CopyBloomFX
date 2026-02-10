#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')
django.setup()

from django.conf import settings
from crypto.paystack_service import PaystackService

print("=== PAYSTACK DEBUG ===")
print(f"SECRET_KEY: {getattr(settings, 'PAYSTACK_SECRET_KEY', 'NOT_FOUND')}")
print(f"PUBLIC_KEY: {getattr(settings, 'PAYSTACK_PUBLIC_KEY', 'NOT_FOUND')}")
print(f"CALLBACK_URL: {getattr(settings, 'PAYSTACK_CALLBACK_URL', 'NOT_FOUND')}")
print()

# Test Paystack service directly
print("=== TESTING PAYSTACK SERVICE ===")
try:
    result = PaystackService.initialize_transaction(
        amount=100,
        email='test@example.com',
        callback_url=getattr(settings, 'PAYSTACK_CALLBACK_URL', ''),
        reference='DEBUG_TEST'
    )
    print(f"Result: {result}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
