# Paystack Setup Guide

## 1. Get Paystack API Keys

1. Sign up at [Paystack](https://paystack.co)
2. Go to Settings > API Keys
3. Copy your **Test Public Key** and **Test Secret Key**
4. For production, use **Live Public Key** and **Live Secret Key**

## 2. Configure Environment Variables

Add these to your environment variables or `.env` file:

```bash
# Test Keys (for development)
PAYSTACK_SECRET_KEY=sk_test_your_actual_secret_key_here
PAYSTACK_PUBLIC_KEY=pk_test_your_actual_public_key_here

# Live Keys (for production)
# PAYSTACK_SECRET_KEY=sk_live_your_actual_secret_key_here
# PAYSTACK_PUBLIC_KEY=pk_live_your_actual_public_key_here

# Callback URL
PAYSTACK_CALLBACK_URL=http://127.0.0.1:8000/paystack/callback/
```

## 3. Test Your Setup

### Test Transaction Initialization:
```python
from crypto.paystack_service import PaystackService

# Test with small amount
result = PaystackService.initialize_transaction(
    amount=100,  # 100 NGN
    email="test@example.com",
    callback_url="http://127.0.0.1:8000/paystack/callback/"
)

if result.get('status'):
    print("✅ Paystack is working!")
    print(f"Authorization URL: {result['data']['authorization_url']}")
else:
    print(f"❌ Error: {result.get('message')}")
```

### Test Webhook:
1. Start your Django server
2. Use a tool like [ngrok](https://ngrok.com) to expose your localhost
3. Add the webhook URL to your Paystack dashboard
4. Test a payment to trigger webhooks

## 4. Common Issues

### Issue: "Invalid API Key"
- **Solution:** Check your secret key format. It should start with `sk_test_` or `sk_live_`

### Issue: "Timeout"
- **Solution:** Check your internet connection and Paystack service status

### Issue: "Webhook not working"
- **Solution:** Ensure your webhook URL is publicly accessible

## 5. Security Notes

- **Never** commit your secret keys to version control
- Use environment variables for all API keys
- Implement proper webhook signature verification in production
- Use HTTPS for your callback URL in production

## 6. Testing Checklist

- [ ] API keys are correctly configured
- [ ] Test transaction initialization works
- [ ] Webhook endpoint is accessible
- [ ] Payment verification works
- [ ] Balance updates correctly after successful payment
- [ ] Error handling works properly

## 7. Production Deployment

1. Switch to live API keys
2. Update callback URL to your production domain
3. Enable webhook signature verification
4. Set up proper logging and monitoring
5. Test with real payments (small amounts first)
