"""
Performance Analysis and Optimization Script for CopyBloom FX
"""
import os
import sys
import time

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_platform.settings')

def analyze_performance():
    print("COPYBLOOM FX PERFORMANCE ANALYSIS")
    print("=" * 50)
    
    try:
        import django
        django.setup()
        
        from django.conf import settings
        from django.contrib.auth.models import User
        from crypto.models import Profile, Deposit, CopyTrade, DailyReward
        from django.db import connection
        from django.test.utils import override_settings
        
        print(f"✅ Django setup successful")
        
        # Check database configuration
        print(f"\n🗄️ Database Configuration:")
        print(f"  - Database engine: {getattr(settings, 'DATABASES', {}).get('default', {}).get('ENGINE', 'Not configured')}")
        print(f"  - Database name: {getattr(settings, 'DATABASES', {}).get('default', {}).get('NAME', 'Not configured')}")
        
        # Check debug mode
        print(f"\n🐛 Debug Settings:")
        print(f"  - DEBUG mode: {getattr(settings, 'DEBUG', 'Not set')}")
        print(f"  - Debug toolbar: {'Installed' if 'debug_toolbar' in settings.INSTALLED_APPS else 'Not installed'}")
        
        # Analyze database size
        print(f"\n📊 Database Statistics:")
        try:
            user_count = User.objects.count()
            profile_count = Profile.objects.count()
            deposit_count = Deposit.objects.count()
            copytrade_count = CopyTrade.objects.count()
            dailyreward_count = DailyReward.objects.count()
            
            print(f"  - Users: {user_count}")
            print(f"  - Profiles: {profile_count}")
            print(f"  - Deposits: {deposit_count}")
            print(f"  - Copy trades: {copytrade_count}")
            print(f"  - Daily rewards: {dailyreward_count}")
            
            total_records = user_count + profile_count + deposit_count + copytrade_count + dailyreward_count
            print(f"  - Total records: {total_records}")
            
            if total_records > 10000:
                print(f"  ⚠️  Large dataset detected - may cause performance issues")
        except Exception as e:
            print(f"  ❌ Error getting database stats: {e}")
        
        # Check for missing indexes
        print(f"\n🔍 Performance Issues:")
        
        # Test slow queries
        slow_queries = []
        
        # Test dashboard performance
        start_time = time.time()
        try:
            # Simulate dashboard queries
            users = User.objects.all()[:10]
            for user in users:
                profile = getattr(user, 'profile', None)
                if profile:
                    deposits = Deposit.objects.filter(user=user)[:5]
                    copytrades = CopyTrade.objects.filter(user=user)[:5]
            
            dashboard_time = time.time() - start_time
            print(f"  - Dashboard query time: {dashboard_time:.3f}s")
            if dashboard_time > 2.0:
                slow_queries.append(f"Dashboard queries ({dashboard_time:.3f}s)")
        except Exception as e:
            print(f"  ❌ Dashboard test error: {e}")
        
        # Test multi-account detection performance
        start_time = time.time()
        try:
            # Simulate multi-account detection
            from crypto.views import detect_and_flag_multiple_accounts
            flagged_count = detect_and_flag_multiple_accounts()
            detection_time = time.time() - start_time
            print(f"  - Multi-account detection time: {detection_time:.3f}s")
            if detection_time > 1.0:
                slow_queries.append(f"Multi-account detection ({detection_time:.3f}s)")
        except Exception as e:
            print(f"  ❌ Multi-account detection test error: {e}")
        
        if slow_queries:
            print(f"  ⚠️  Slow operations detected:")
            for query in slow_queries:
                print(f"    - {query}")
        else:
            print(f"  ✅ No major performance issues detected")
        
        # Check for optimization opportunities
        print(f"\n🚀 Optimization Recommendations:")
        
        # Check if DEBUG is on
        if getattr(settings, 'DEBUG', False):
            print(f"  1. 🔧 Turn off DEBUG mode in production")
            print(f"     - DEBUG=True adds significant overhead")
            print(f"     - Set DEBUG=False in settings.py")
        
        # Check for database indexes
        print(f"  2. 📈 Add database indexes for frequently queried fields:")
        print(f"     - User.last_login_ip")
        print(f"     - User.phone")
        print(f"     - Deposit.user")
        print(f"     - CopyTrade.user")
        print(f"     - Profile.user")
        
        # Check for caching
        print(f"  3. 🗄️ Implement caching:")
        print(f"     - Cache user ranks")
        print(f"     - Cache daily profits")
        print(f"     - Cache referral statistics")
        
        # Check for query optimization
        print(f"  4. ⚡ Optimize database queries:")
        print(f"     - Use select_related() for foreign keys")
        print(f"     - Use prefetch_related() for many-to-many")
        print(f"     - Use only() to limit fields")
        
        # Check for background tasks
        print(f"  5. 🔄 Implement background tasks:")
        print(f"     - Move multi-account detection to background")
        print(f"     - Schedule daily profit generation")
        print(f"     - Process expired deposits asynchronously")
        
        # Check media files
        print(f"  6. 📁 Optimize media serving:")
        print(f"     - Use CDN for profile pictures")
        print(f"     - Compress images before upload")
        print(f"     - Implement lazy loading")
        
        print(f"\n🎯 Quick Fixes:")
        print(f"  1. Set DEBUG=False in settings.py")
        print(f"  2. Add database indexes")
        print(f"  3. Implement caching")
        print(f"  4. Optimize dashboard queries")
        
        print(f"\n✅ Performance analysis completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    analyze_performance()
