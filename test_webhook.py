#!/usr/bin/env python
"""
Test script to simulate Paystack webhooks
"""
import requests
import json
import time

def test_webhook():
    """Test the Paystack webhook endpoint"""
    
    # First, let's create a test deposit to simulate
    webhook_url = "http://127.0.0.1:8000/paystack/callback/"
    test_webhook_url = "http://127.0.0.1:8000/test-webhook/"
    
    print("=== PAYSTACK WEBHOOK TEST ===")
    print(f"Webhook URL: {webhook_url}")
    print(f"Test Webhook URL: {test_webhook_url}")
    print()
    
    # Test webhook status
    print("1. Checking webhook status...")
    try:
        response = requests.get("http://127.0.0.1:8000/webhook-status/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # Test webhook with sample payload
    print("2. Testing webhook with sample payload...")
    
    # First, let's find a real deposit reference to test with
    sample_payload = {
        "event": "charge.success",
        "data": {
            "reference": "TEST_DEMO_123456",
            "status": "success",
            "amount": 10000,  # 100 NGN in kobo
            "currency": "NGN",
            "customer": {
                "email": "test@example.com",
                "first_name": "Test",
                "last_name": "User"
            },
            "metadata": {
                "custom_fields": []
            },
            "paid_at": int(time.time()),
            "created_at": int(time.time())
        }
    }
    
    try:
        # Test the test webhook endpoint first
        print("Testing test-webhook endpoint...")
        response = requests.post(
            test_webhook_url,
            json=sample_payload,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        print(f"Test Webhook Status: {response.status_code}")
        print(f"Test Webhook Response: {json.dumps(response.json(), indent=2)}")
        
        print()
        
        # Test the actual webhook endpoint
        print("Testing actual webhook endpoint...")
        response = requests.post(
            webhook_url,
            json=sample_payload,
            headers={
                'Content-Type': 'application/json',
                'x-paystack-signature': 'test-signature'
            },
            timeout=10
        )
        print(f"Actual Webhook Status: {response.status_code}")
        print(f"Actual Webhook Response: {json.dumps(response.json(), indent=2)}")
        
    except Exception as e:
        print(f"Error testing webhook: {e}")
    
    print()
    print("=== INSTRUCTIONS FOR REAL WEBHOOK TESTING ===")
    print("1. Install ngrok: pip install pyngrok")
    print("2. Run: ngrok http 8000")
    print("3. Copy the ngrok URL (e.g., https://abc123.ngrok.io)")
    print("4. Go to Paystack Dashboard → Settings → Webhooks")
    print("5. Add webhook URL: https://abc123.ngrok.io/paystack/callback/")
    print("6. Test with a real Paystack payment")
    print("7. Check server logs for DEBUG messages")

if __name__ == "__main__":
    test_webhook()
