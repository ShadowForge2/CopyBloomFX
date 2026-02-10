#!/usr/bin/env python
"""
Direct Paystack test - working version!
"""
import requests
import json

def test_paystack_direct():
    """Test Paystack API directly with your working keys"""
    
    # Your working keys
    SECRET_KEY = "sk_test_176a7ac484646630cd54679b52493259c4dd1d7c"
    PUBLIC_KEY = "pk_test_bc74895bd1a860928f3e2ed4e9052d8f01e16c76"
    
    print("=== DIRECT PAYSTACK TEST ===")
    print(f"Secret Key: {SECRET_KEY[:20]}...")
    print(f"Public Key: {PUBLIC_KEY[:20]}...")
    
    # Test API call
    headers = {
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json",
    }
    
    data = {
        "amount": 10000,  # 100 NGN in kobo
        "email": "test@example.com",
        "reference": "TEST_DIRECT_123",
        "callback_url": "http://127.0.0.1:8000/paystack/callback/",
        "currency": "NGN",
    }
    
    try:
        response = requests.post(
            "https://api.paystack.co/transaction/initialize",
            headers=headers,
            json=data,
            timeout=30
        )
        
        result = response.json()
        
        print(f"\nStatus Code: {response.status_code}")
        print(f"Response: {json.dumps(result, indent=2)}")
        
        if result.get('status'):
            print("\n✅ PAYSTACK IS WORKING PERFECTLY!")
            print(f"✅ Authorization URL: {result['data']['authorization_url']}")
            print(f"✅ Access Code: {result['data']['access_code']}")
            print(f"✅ Reference: {result['data']['reference']}")
            return True
        else:
            print(f"\n❌ Error: {result.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"\n❌ Exception: {e}")
        return False

if __name__ == "__main__":
    test_paystack_direct()
