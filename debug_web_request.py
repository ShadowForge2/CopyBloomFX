#!/usr/bin/env python
import os
import sys

# Check if .env file exists and what it contains
print("=== .env FILE DEBUG ===")
env_file = '.env'
if os.path.exists(env_file):
    with open(env_file, 'r') as f:
        for i, line in enumerate(f, 1):
            if 'PAYSTACK' in line:
                print(f"Line {i}: {line.strip()}")
else:
    print(".env file not found!")

print("\n=== ENVIRONMENT VARIABLES ===")
print(f"PAYSTACK_SECRET_KEY: {os.environ.get('PAYSTACK_SECRET_KEY', 'NOT_SET')}")
print(f"PAYSTACK_PUBLIC_KEY: {os.environ.get('PAYSTACK_PUBLIC_KEY', 'NOT_SET')}")

# Try loading dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("\n=== AFTER LOADING DOTENV ===")
    print(f"PAYSTACK_SECRET_KEY: {os.environ.get('PAYSTACK_SECRET_KEY', 'NOT_SET')}")
    print(f"PAYSTACK_PUBLIC_KEY: {os.environ.get('PAYSTACK_PUBLIC_KEY', 'NOT_SET')}")
except ImportError:
    print("\npython-dotenv not available")
