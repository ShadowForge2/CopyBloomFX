#!/usr/bin/env python
"""
Quick InfinityFree Deployment Package Creator
"""
import os
import shutil
import zipfile

def create_deployment_package():
    """Create a zip file for InfinityFree deployment"""
    
    print("Creating InfinityFree deployment package...")
    
    # Create deployment directory
    deploy_dir = "infinityfree_deploy"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Files to copy
    files_to_copy = [
        ('crypto/', 'crypto/'),
        ('crypto_platform/', 'crypto_platform/'),
        ('manage.py', 'manage.py'),
        ('requirements.txt', 'requirements.txt'),
        ('.htaccess', '.htaccess'),
        ('index.php', 'index.php'),
        ('infinityfree_settings.py', 'infinityfree_settings.py'),
        ('migrate.php', 'migrate.php'),
        ('.env', '.env'),
    ]
    
    # Copy files
    for src, dst in files_to_copy:
        if os.path.exists(src):
            if os.path.isdir(src):
                shutil.copytree(src, os.path.join(deploy_dir, dst))
            else:
                shutil.copy2(src, os.path.join(deploy_dir, dst))
            print(f"Copied: {src}")
        else:
            print(f"Missing: {src}")
    
    # Create zip file
    zip_filename = "infinityfree_crypto_platform.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(deploy_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, deploy_dir)
                zipf.write(file_path, arcname)
    
    print(f"\nDeployment package created: {zip_filename}")
    print(f"Size: {os.path.getsize(zip_filename) / 1024 / 1024:.2f} MB")
    
    return zip_filename

def show_instructions():
    """Show deployment instructions"""
    
    print("\n" + "="*60)
    print("INFINITYFREE DEPLOYMENT INSTRUCTIONS")
    print("="*60)
    
    print("\n1. CREATE INFINITYFREE ACCOUNT:")
    print("   - Go to: https://infinityfree.net/")
    print("   - Sign up for free account")
    print("   - Create hosting account")
    print("   - Choose subdomain (e.g., crypto-invest.epizy.com)")
    
    print("\n2. UPLOAD FILES:")
    print("   - Download FileZilla")
    print("   - Connect to: ftpupload.epizy.com")
    print("   - Upload infinityfree_crypto_platform.zip contents to public_html/")
    
    print("\n3. SET UP DATABASE:")
    print("   - Go to InfinityFree Control Panel")
    print("   - Click 'MySQL Database'")
    print("   - Create database: crypto_platform")
    print("   - Visit: https://your-domain.epizy.com/migrate.php")
    
    print("\n4. UPDATE SETTINGS:")
    print("   - Edit infinityfree_settings.py")
    print("   - Update database credentials")
    print("   - Update your domain name")
    
    print("\n5. TEST YOUR SITE:")
    print("   - Visit: https://your-domain.epizy.com")
    print("   - Test registration and deposits")
    
    print("\nYour platform will be live at: https://your-domain.epizy.com")

if __name__ == "__main__":
    # Create deployment package
    package_file = create_deployment_package()
    
    # Show instructions
    show_instructions()
    
    print(f"\nReady to deploy! Upload the contents of {package_file.replace('.zip', '')} to InfinityFree.")
