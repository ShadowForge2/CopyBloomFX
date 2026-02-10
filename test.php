<?php
// Simple test file to check if server works
echo "<!DOCTYPE html>
<html>
<head>
    <title>Server Test - CopyBloom FX</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 800px; margin: 0 auto; text-align: center; }
        .status { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin: 20px 0; }
        .success { background: rgba(76,175,80,0.2); }
        .info { background: rgba(33,150,243,0.2); }
        .btn { display: inline-block; padding: 15px 30px; background: #4CAF50; color: white; text-decoration: none; border-radius: 5px; margin: 10px; }
    </style>
</head>
<body>
    <div class='container'>
        <h1>🚀 CopyBloom FX Platform</h1>
        
        <div class='status success'>
            <h2>✅ Server is Working!</h2>
            <p>Your hosting is active and PHP is running correctly.</p>
        </div>
        
        <div class='status info'>
            <h3>📋 Platform Status:</h3>
            <p><strong>Domain:</strong> copybloomfx.great-site.net</p>
            <p><strong>Server:</strong> InfinityFree</p>
            <p><strong>Status:</strong> Ready for Configuration</p>
        </div>
        
        <div class='status info'>
            <h3>🔧 Next Steps:</h3>
            <p>1. Set up database tables</p>
            <p>2. Configure Django settings</p>
            <p>3. Test payment system</p>
            <p>4. Launch platform</p>
        </div>
        
        <div style='margin-top: 30px;'>
            <a href='/migrate.php' class='btn'>🗄️ Set Up Database</a>
            <a href='/admin/' class='btn'>🔐 Admin Panel</a>
        </div>
        
        <div style='margin-top: 40px; font-size: 0.9em; opacity: 0.8;'>
            <p>CopyBloom FX Crypto Investment Platform</p>
            <p>© 2026 All Rights Reserved</p>
        </div>
    </div>
</body>
</html>";
?>
