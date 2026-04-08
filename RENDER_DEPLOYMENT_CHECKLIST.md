# RENDER DEPLOYMENT CHECKLIST

## PRE-DEPLOYMENT STEPS

### 1. GitHub Repository
- [x] Repository pushed to GitHub: https://github.com/ShadowForge2/CopyBloomFX.git
- [x] All latest changes committed and pushed
- [x] render.yaml file exists in root directory

### 2. Environment Variables
- [x] SECRET_KEY generated: `n6vm0&858vox-!_2#@bstzl%*li4+epamik%9lp2dy_0qgbxh8`
- [x] Environment variables file created: `RENDER_ENVIRONMENT_VARIABLES.txt`
- [ ] Paystack LIVE keys obtained from https://dashboard.paystack.co/settings/api_keys

### 3. Configuration Files
- [x] render_settings.py configured for production
- [x] render.yaml service configuration ready
- [x] Admin session timeout implemented
- [x] Referral system working

## RENDER DEPLOYMENT STEPS

### 1. Create Render Account
1. Go to https://render.com
2. Sign up with GitHub (recommended)
3. Connect your GitHub repository

### 2. Create PostgreSQL Database
1. Click "New +" -> "PostgreSQL"
2. Name: `crypto-db`
3. Database name: `crypto_prod`
4. User: `postgres`
5. Choose region closest to your users
6. Click "Create Database"
7. **DATABASE_URL will be automatically added to environment variables**

### 3. Create Web Service
1. Click "New +" -> "Web Service"
2. Connect your GitHub repository: `ShadowForge2/CopyBloomFX`
3. **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. **Start Command**: `gunicorn crypto_platform.wsgi:application`
5. **Runtime**: Python 3
6. Click "Advanced Settings"
7. **Auto-Deploy**: Enable (optional)

### 4. Add Environment Variables
1. Go to your Web Service -> "Environment" tab
2. Add these variables:

```
SECRET_KEY=n6vm0&858vox-!_2#@bstzl%*li4+epamik%9lp2dy_0qgbxh8
DJANGO_SETTINGS_MODULE=crypto_platform.render_settings
PAYSTACK_SECRET_KEY=sk_live_your_live_secret_key_here
PAYSTACK_PUBLIC_KEY=pk_live_your_live_public_key_here
```

3. DATABASE_URL should already be there (from PostgreSQL service)

### 5. Deploy
1. Click "Create Web Service"
2. Wait for deployment to complete
3. Test your application

## POST-DEPLOYMENT STEPS

### 1. Initial Setup
1. Access your app: `https://your-app-name.onrender.com`
2. Create superuser admin account
3. Test admin login: `/admin/login/`
4. Test referral system
5. Test Paystack integration

### 2. Paystack Configuration
1. Update Paystack webhook URL in Paystack dashboard:
   - Webhook URL: `https://your-app-name.onrender.com/paystack/callback/`
2. Test with Paystack TEST keys first
3. Switch to LIVE keys when ready

### 3. Custom Domain (Optional)
1. Add custom domain in Render dashboard
2. Update DNS records
3. Update BASE_URL in environment variables

### 4. Monitoring
1. Check Render logs for any errors
2. Monitor database usage
3. Set up alerts (optional)

## TROUBLESHOOTING

### Common Issues:
1. **Database Connection Error**: Check DATABASE_URL format
2. **Static Files Not Loading**: Run `collectstatic` command
3. **Paystack Webhook Failing**: Update webhook URL in Paystack dashboard
4. **Admin Login Not Working**: Check DJANGO_SETTINGS_MODULE

### Debug Commands:
```bash
# Check logs
render logs

# SSH into instance
render ssh

# Run Django commands
python manage.py migrate
python manage.py createsuperuser
```

## SECURITY NOTES

### Required for Production:
- [x] DEBUG=False in render_settings.py
- [x] SECURE_SSL_REDIRECT=True
- [x] SESSION_COOKIE_SECURE=True
- [x] CSRF_COOKIE_SECURE=True
- [x] Custom SECRET_KEY generated

### Recommended:
- [ ] Enable SSL certificate (Render provides free SSL)
- [ ] Set up monitoring and alerts
- [ ] Regular database backups
- [ ] Use environment variables for all secrets

## COST ESTIMATION

### Render Free Tier:
- PostgreSQL: $0/month (up to 90 days)
- Web Service: $0/month (750 hours/month)
- **Total**: $0/month for basic usage

### Paid Tier (if needed):
- PostgreSQL: ~$7/month
- Web Service: ~$7/month
- **Total**: ~$14/month

## QUICK COPY-PASTE ENVIRONMENT VARIABLES:

```
SECRET_KEY=n6vm0&858vox-!_2#@bstzl%*li4+epamik%9lp2dy_0qgbxh8
DJANGO_SETTINGS_MODULE=crypto_platform.render_settings
PAYSTACK_SECRET_KEY=sk_live_your_live_secret_key_here
PAYSTACK_PUBLIC_KEY=pk_live_your_live_public_key_here
```

## DEPLOYMENT URL FORMAT

Your app will be available at:
`https://your-app-name.onrender.com`

Replace `your-app-name` with whatever you name your Render service.
