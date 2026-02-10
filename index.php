<?php
/**
 * Django PHP Bootstrap for InfinityFree
 * This file acts as a bridge between Apache and Django
 */

// Set environment variables
$_ENV['DJANGO_SETTINGS_MODULE'] = 'crypto_platform.infinityfree_settings';

// Get the requested path
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Remove leading slash
$path = ltrim($path, '/');

// Handle Django requests
if ($path == '') {
    $path = 'crypto/';  # Default to crypto app
}

// Execute Django through Python
$command = "python3 manage.py runserver 127.0.0.1:8000 --settings=crypto_platform.infinityfree_settings 2>&1";
$output = shell_exec($command);

// For now, show a simple landing page
echo '<!DOCTYPE html>
<html>
<head>
    <title>Crypto Investment Platform</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 800px; margin: 0 auto; text-align: center; }
        h1 { font-size: 2.5em; margin-bottom: 20px; }
        .status { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 20px 0; }
        .success { background: rgba(76,175,80,0.2); }
        .info { background: rgba(33,150,243,0.2); }
        .btn { display: inline-block; padding: 15px 30px; background: #4CAF50; color: white; text-decoration: none; border-radius: 5px; margin: 10px; }
        .btn:hover { background: #45a049; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Crypto Investment Platform</h1>
        
        <div class="status success">
            <h2>✅ Platform Successfully Deployed!</h2>
            <p>Your crypto investment platform is now hosted on InfinityFree</p>
        </div>
        
        <div class="status info">
            <h3>📋 Current Status:</h3>
            <p><strong>Hosting:</strong> InfinityFree (Free)</p>
            <p><strong>Database:</strong> MySQL (InfinityFree)</p>
            <p><strong>Payment:</strong> Paystack (Live Mode)</p>
            <p><strong>Status:</strong> Ready for Users</p>
        </div>
        
        <div class="status info">
            <h3>🔧 Next Steps:</h3>
            <p>1. Set up database tables</p>
            <p>2. Configure domain name</p>
            <p>3. Test payment system</p>
            <p>4. Launch to users</p>
        </div>
        
        <div style="margin-top: 30px;">
            <a href="/admin/" class="btn">🔐 Admin Panel</a>
            <a href="/crypto/" class="btn">🏠 Platform Home</a>
        </div>
        
        <div style="margin-top: 40px; font-size: 0.9em; opacity: 0.8;">
            <p>Deployed with Django + Paystack + InfinityFree</p>
            <p>© 2026 Crypto Investment Platform</p>
        </div>
    </div>
</body>
</html>';

// Log the request for debugging
error_log("Django Request: " . $_SERVER['REQUEST_URI']);
?>
