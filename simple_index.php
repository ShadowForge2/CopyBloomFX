<?php
// Simple landing page for CopyBloom FX
session_start();

// Handle basic form submissions
if ($_POST['action'] == 'register') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    
    if ($name && $email && $password) {
        // Store user in session (simulating registration)
        $_SESSION['user_name'] = $name;
        $_SESSION['user_email'] = $email;
        $_SESSION['logged_in'] = true;
        
        // Redirect to dashboard
        header('Location: /simple_dashboard.php');
        exit();
    } else {
        $message = "❌ Please fill in all fields to register.";
    }
} elseif ($_POST['action'] == 'login') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    
    if ($email && $password) {
        // For demo, accept any email/password (in real app, verify against database)
        $name = explode('@', $email)[0]; // Get name from email
        $_SESSION['user_name'] = ucfirst($name);
        $_SESSION['user_email'] = $email;
        $_SESSION['logged_in'] = true;
        
        // Redirect to dashboard
        header('Location: /simple_dashboard.php');
        exit();
    } else {
        $message = "❌ Please enter your email and password.";
    }
}

// Handle logout from main page
if (isset($_GET['logout']) && $_GET['logout'] === 'true') {
    session_destroy();
    $message = "✅ You have been logged out successfully.";
}

echo "<!DOCTYPE html>
<html>
<head>
    <title>CopyBloom FX - Crypto Investment Platform</title>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; color: white; margin-bottom: 40px; }
        .header h1 { font-size: 3em; margin-bottom: 10px; }
        .header p { font-size: 1.2em; opacity: 0.9; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 40px; }
        .feature { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; text-align: center; color: white; }
        .feature h3 { font-size: 1.5em; margin-bottom: 15px; }
        .cta { text-align: center; color: white; }
        .cta h2 { font-size: 2em; margin-bottom: 20px; }
        .btn { display: inline-block; padding: 15px 30px; background: #4CAF50; color: white; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold; }
        .btn:hover { background: #45a049; }
        .btn-secondary { background: #ff9800; }
        .btn-secondary:hover { background: #e68900; }
        .message { background: rgba(76,175,80,0.2); padding: 15px; border-radius: 5px; margin: 20px 0; text-align: center; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 40px 0; }
        .stat { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; text-align: center; color: white; }
        .stat h4 { font-size: 2em; margin-bottom: 5px; }
        .footer { text-align: center; color: white; margin-top: 60px; opacity: 0.8; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h1>🚀 CopyBloom FX</h1>
            <p>Professional Crypto Investment Platform</p>
        </div>";

if (isset($message)) {
    echo "<div class='message'>$message</div>";
}

echo "
        <div class='features'>
            <div class='feature'>
                <h3>💰 Copy Trading</h3>
                <p>Copy successful traders and earn like the pros</p>
            </div>
            <div class='feature'>
                <h3>📈 Multiple Ranks</h3>
                <p>Progress from Green Horn to Market Wizard</p>
            </div>
            <div class='feature'>
                <h3>🔒 Secure Payments</h3>
                <p>Paystack integration for safe deposits</p>
            </div>
            <div class='feature'>
                <h3>🎯 Daily Profits</h3>
                <p>Earn consistent daily returns on investments</p>
            </div>
            <div class='feature'>
                <h3>👥 Referral System</h3>
                <p>Earn bonuses by referring new users</p>
            </div>
            <div class='feature'>
                <h3>📊 Real-time Analytics</h3>
                <p>Track your investments and profits</p>
            </div>
        </div>

        <div class='stats'>
            <div class='stat'>
                <h4>5%</h4>
                <p>Daily Profit</p>
            </div>
            <div class='stat'>
                <h4>6</h4>
                <p>Rank Levels</p>
            </div>
            <div class='stat'>
                <h4>24/7</h4>
                <p>Trading</p>
            </div>
            <div class='stat'>
                <h4>100%</h4>
                <p>Secure</p>
            </div>
        </div>

        <div class='cta'>";

// Check if user is already logged in
if (isset($_SESSION['logged_in']) && $_SESSION['logged_in'] === true) {
    echo "<h2>� Welcome Back!</h2>
          <p>You are already logged in as " . $_SESSION['user_name'] . "</p>
          <a href='/simple_dashboard.php' class='btn'>📊 Go to Dashboard</a>
          <a href='/?logout=true' class='btn btn-secondary'>🚪 Logout</a>";
} else {
    echo "<h2>� Start Your Crypto Journey Today!</h2>
          <p>Join thousands of successful investors</p>";
    
    if (isset($message)) {
        echo "<div style='background: rgba(76,175,80,0.9); color: white; padding: 15px; border-radius: 8px; margin: 20px auto; max-width: 500px; text-align: center; font-weight: bold;'>$message</div>";
    }

    echo "            
            <!-- Registration Form -->
            <div style='background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 20px 0;'>
                <h3 style='color: white; margin-bottom: 20px;'>🚀 Create Account</h3>
                <form method='POST' style='max-width: 400px; margin: 0 auto;'>
                    <input type='hidden' name='action' value='register'>
                    <div style='margin-bottom: 15px;'>
                        <input type='text' name='name' placeholder='Full Name' required 
                               style='width: 100%; padding: 12px; border: none; border-radius: 5px; font-size: 16px;'>
                    </div>
                    <div style='margin-bottom: 15px;'>
                        <input type='email' name='email' placeholder='Email Address' required 
                               style='width: 100%; padding: 12px; border: none; border-radius: 5px; font-size: 16px;'>
                    </div>
                    <div style='margin-bottom: 15px;'>
                        <input type='password' name='password' placeholder='Password' required 
                               style='width: 100%; padding: 12px; border: none; border-radius: 5px; font-size: 16px;'>
                    </div>
                    <button type='submit' class='btn' style='width: 100%;'>Create Account</button>
                </form>
            </div>
            
            <!-- Login Form -->
            <div style='background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; margin: 20px 0;'>
                <h3 style='color: white; margin-bottom: 20px;'>🔐 Login</h3>
                <form method='POST' style='max-width: 400px; margin: 0 auto;'>
                    <input type='hidden' name='action' value='login'>
                    <div style='margin-bottom: 15px;'>
                        <input type='email' name='email' placeholder='Email Address' required 
                               style='width: 100%; padding: 12px; border: none; border-radius: 5px; font-size: 16px;'>
                    </div>
                    <div style='margin-bottom: 15px;'>
                        <input type='password' name='password' placeholder='Password' required 
                               style='width: 100%; padding: 12px; border: none; border-radius: 5px; font-size: 16px;'>
                    </div>
                    <button type='submit' class='btn btn-secondary' style='width: 100%;'>Login</button>
                </form>
            </div>
        </div>
    }
}

        <div class='footer'>
            <p>&copy; 2026 CopyBloom FX. All rights reserved.</p>
            <p>Powered by advanced blockchain technology</p>
        </div>
    </div>
</body>
</html>";
?>
