# 🎯 COMPLETE PAYSTACK SETUP GUIDE

## 📍 WHERE TO ADD YOUR CREDENTIALS

### 1. GET YOUR PAYSTACK KEYS
1. Go to [Paystack Dashboard](https://dashboard.paystack.co)
2. Click **Settings** → **API Keys**
3. Copy your **Test Keys**:
   - **Secret Key**: `sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - **Public Key**: `pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### 2. ADD KEYS TO .env FILE
**File Location:** `django_crypto\.env`

```bash
# Paystack Configuration (Test Mode)
PAYSTACK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PAYSTACK_PUBLIC_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PAYSTACK_CALLBACK_URL=http://127.0.0.1:8000/paystack/callback/

# Django Configuration
DEBUG=True
SECRET_KEY=your-django-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

### 3. INSTALL DEPENDENCIES
**Run this command in your project folder:**
```bash
python -m pip install python-dotenv
```

### 4. WEBHOOK CONFIGURATION

#### For Local Testing (Development):
1. **Use ngrok** to expose your localhost:
   ```bash
   # Install ngrok
   # Download from: https://ngrok.com/download
   
   # Run ngrok
   ngrok http 8000
   ```

2. **Add webhook URL to Paystack:**
   - Go to Paystack Dashboard → Settings → Webhooks
   - Add: `https://your-ngrok-url.ngrok.io/paystack/callback/`

#### For Production:
1. **Add webhook URL to Paystack:**
   - `https://yourdomain.com/paystack/callback/`

## 🧪 TESTING YOUR SETUP

### 1. Test Configuration:
**Visit:** http://127.0.0.1:8000/paystack-test/
- Click "Test Paystack Configuration"
- Should show ✅ for both keys

### 2. Test Payment:
1. Go to http://127.0.0.1:8000/finance/
2. Click **Local Deposit** tab
3. Enter amount (e.g., $10)
4. Click **Submit Deposit**
5. You should be redirected to Paystack payment page

### 3. Test Webhook:
1. Complete a test payment
2. Check if deposit status changes to "paid"
3. Check Django logs for webhook processing

## 📁 FILE LOCATIONS SUMMARY

```
django_crypto/
├── .env                           # ← ADD YOUR KEYS HERE
├── crypto_platform/settings.py   # ✅ Already configured
├── crypto/
│   ├── paystack_service.py       # ✅ Enhanced service
│   ├── views.py                   # ✅ Paystack endpoints
│   ├── urls.py                   # ✅ URL patterns
│   └── templates/
│       └── crypto/
│           ├── paystack_test.html # ✅ Test page
│           └── finance.html       # ✅ Local deposit form
└── SETUP_PAYSTACK.md             # ✅ Setup guide
```

## 🔧 QUICK SETUP CHECKLIST

- [ ] **Get Paystack keys** from dashboard
- [ ] **Add keys to .env file** 
- [ ] **Install python-dotenv** package
- [ ] **Configure webhook** (ngrok for local)
- [ ] **Test configuration** at `/paystack-test/`
- [ ] **Test payment** through finance page
- [ ] **Verify webhook** processing

## 🚨 IMPORTANT NOTES

### Security:
- **Never** commit `.env` file to version control
- **Never** share your secret keys
- **Use different keys** for test and production

### Webhook:
- **Must be publicly accessible** for Paystack to reach it
- **Use HTTPS** in production
- **Test with ngrok** for local development

### Testing:
- **Use test keys** for development
- **Make small test payments** (₦100)
- **Check logs** for debugging

## 🎯 NEXT STEPS

1. **Add your actual Paystack keys** to `.env` file
2. **Run the server**: `python manage.py runserver`
3. **Test configuration**: Visit `/paystack-test/`
4. **Test payment**: Try a local deposit
5. **Monitor logs**: Check webhook processing

## 🆘 TROUBLESHOOTING

### Issue: "Keys not configured"
- **Solution:** Check `.env` file and ensure keys are correct format

### Issue: "Webhook not working"
- **Solution:** Use ngrok for local testing, ensure URL is accessible

### Issue: "Payment fails"
- **Solution:** Check Paystack dashboard for transaction details

### Issue: "Balance not updated"
- **Solution:** Check webhook processing in Django logs

---

**🎉 YOUR PAYSTACK INTEGRATION IS NOW READY!**

**Follow this guide step by step and your payment system will work perfectly!** 💰✨
