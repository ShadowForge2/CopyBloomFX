"""
Quick Performance Check for CopyBloom FX
"""
import os
import sys

# Add the project directory to the Python path
project_path = r'c:\Users\1`030 G4\OneDrive\Desktop\MY PROJECTS\COPY BLOOM INVESTMENT DATABASE\django_crypto'
sys.path.insert(0, project_path)

def quick_performance_check():
    print("COPYBLOOM FX PERFORMANCE CHECK")
    print("=" * 50)
    
    # Check settings file
    settings_file = os.path.join(project_path, 'crypto_platform', 'settings.py')
    if os.path.exists(settings_file):
        print(f"Settings file found: {settings_file}")
        
        # Read settings to check DEBUG mode
        with open(settings_file, 'r') as f:
            content = f.read()
            if 'DEBUG = True' in content:
                print(f"WARNING: DEBUG mode is ON - This causes significant performance overhead")
            else:
                print(f"GOOD: DEBUG mode appears to be OFF")
            
            if 'debug_toolbar' in content:
                print(f"WARNING: Debug toolbar installed - Can slow down requests")
    else:
        print(f"ERROR: Settings file not found")
    
    # Check database size
    db_file = os.path.join(project_path, 'db.sqlite3')
    if os.path.exists(db_file):
        size_mb = os.path.getsize(db_file) / (1024 * 1024)
        print(f"Database file: {size_mb:.2f} MB")
        
        if size_mb > 100:
            print(f"WARNING: Large database detected - May cause performance issues")
        elif size_mb > 50:
            print(f"WARNING: Medium database - Consider optimization")
        else:
            print(f"GOOD: Database size is reasonable")
    else:
        print(f"INFO: Database file not found")
    
    # Check media directory
    media_dir = os.path.join(project_path, 'media')
    if os.path.exists(media_dir):
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk(media_dir):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        size_mb = total_size / (1024 * 1024)
        print(f"Media directory: {size_mb:.2f} MB, {file_count} files")
        
        if size_mb > 500:
            print(f"WARNING: Large media files - Consider compression or CDN")
    else:
        print(f"INFO: Media directory not created yet")
    
    print(f"\nCOMMON PERFORMANCE ISSUES:")
    print(f"1. DEBUG mode ON - Adds 50-100% overhead")
    print(f"2. No database indexes - Slow queries on large datasets")
    print(f"3. Multi-account detection on every request - CPU intensive")
    print(f"4. No caching - Repeated calculations")
    print(f"5. Large media files - Slow loading")
    
    print(f"\nQUICK FIXES:")
    print(f"1. Set DEBUG=False in settings.py")
    print(f"2. Reduce multi-account detection frequency")
    print(f"3. Add database indexes")
    print(f"4. Implement basic caching")
    
    print(f"\nIMMEDIATE ACTIONS:")
    print(f"1. Check if DEBUG=True in settings.py")
    print(f"2. Monitor server CPU usage")
    print(f"3. Check database query times")
    print(f"4. Test response times with/without multi-account detection")

if __name__ == "__main__":
    quick_performance_check()
