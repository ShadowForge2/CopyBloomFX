#!/usr/bin/env python
"""
Create single ZIP file for InfinityFree upload
"""
import os
import zipfile
import shutil

def create_upload_package():
    """Create a single ZIP file with everything needed"""
    
    print("Creating complete upload package...")
    
    # Create deployment directory
    deploy_dir = "complete_upload"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Files and folders to include
    items_to_copy = [
        'crypto',
        'crypto_platform', 
        'manage.py',
        'requirements.txt',
        '.htaccess',
        'index.php',
        'infinityfree_settings.py',
        'migrate.php',
        '.env'
    ]
    
    print("Copying files...")
    copied_count = 0
    
    for item in items_to_copy:
        if os.path.exists(item):
            dest_path = os.path.join(deploy_dir, item)
            if os.path.isdir(item):
                shutil.copytree(item, dest_path)
                print(f"Copied folder: {item}")
            else:
                shutil.copy2(item, dest_path)
                print(f"Copied file: {item}")
            copied_count += 1
        else:
            print(f"Missing: {item}")
    
    # Create ZIP file
    zip_filename = "CRYPTO_PLATFORM_COMPLETE.zip"
    print(f"\nCreating ZIP file: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(deploy_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, deploy_dir)
                zipf.write(file_path, arcname)
    
    # Get file size
    file_size = os.path.getsize(zip_filename) / 1024 / 1024
    
    print(f"\n" + "="*60)
    print("UPLOAD PACKAGE CREATED SUCCESSFULLY!")
    print("="*60)
    print(f"File: {zip_filename}")
    print(f"Size: {file_size:.2f} MB")
    print(f"Items copied: {copied_count}")
    print(f"Ready for InfinityFree upload!")
    
    return zip_filename

def show_upload_instructions():
    """Show how to upload the ZIP file"""
    
    print("\n" + "="*60)
    print("HOW TO UPLOAD TO INFINITYFREE")
    print("="*60)
    
    print("\n1. CREATE INFINITYFREE ACCOUNT:")
    print("   - Go to: https://infinityfree.net/")
    print("   - Sign up for free account")
    print("   - Create hosting account")
    print("   - Choose subdomain (e.g., crypto-invest.epizy.com)")
    
    print("\n2. UPLOAD ZIP FILE:")
    print("   - Go to InfinityFree Control Panel")
    print("   - Click 'File Manager'")
    print("   - Navigate to public_html/")
    print("   - Click 'Upload'")
    print("   - Select: CRYPTO_PLATFORM_COMPLETE.zip")
    print("   - Click 'Extract' to unzip all files")
    
    print("\n3. ALTERNATIVE - FTP UPLOAD:")
    print("   - Download FileZilla")
    print("   - Connect to: ftpupload.epizy.com")
    print("   - Upload CRYPTO_PLATFORM_COMPLETE.zip")
    print("   - Right-click ZIP file → Extract")
    
    print("\n4. SET UP DATABASE:")
    print("   - Control Panel → MySQL Database")
    print("   - Create database: crypto_platform")
    print("   - Visit: https://your-domain.epizy.com/migrate.php")
    
    print("\n5. UPDATE SETTINGS:")
    print("   - Edit infinityfree_settings.py in File Manager")
    print("   - Update database credentials")
    print("   - Update your domain name")
    
    print("\n6. TEST YOUR SITE:")
    print("   - Visit: https://your-domain.epizy.com")
    print("   - Test registration and deposits")
    
    print("\n" + "="*60)
    print("YOUR PLATFORM WILL BE LIVE AT:")
    print("https://your-subdomain.epizy.com")
    print("="*60)

if __name__ == "__main__":
    # Create the upload package
    zip_file = create_upload_package()
    
    # Show instructions
    show_upload_instructions()
    
    print(f"\nReady! Upload {zip_file} to InfinityFree and extract!")
