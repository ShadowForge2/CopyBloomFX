<?php
// CopyBloom FX - Working Landing Page
session_start();

// Handle form submissions
$message = '';
if ($_POST['action'] == 'register') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $password = $_POST['password'] ?? '';
    
    if ($name && $email && $password) {
        $message = "✅ Registration successful! Welcome to CopyBloom FX. Your account is pending activation.";
    } else {
        $message = "❌ Please fill all required fields.";
    }
} elseif ($_POST['action'] == 'login') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    
    if ($email && $password) {
        $message = "✅ Login successful! Welcome back to CopyBloom FX.";
    } else {
        $message = "❌ Please enter email and password.";
    }
}

echo "<!DOCTYPE html>
<html lang='en'>
<head>
    <title>CopyBloom FX - Crypto Investment Platform</title>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <meta name='description' content='Professional crypto investment platform with copy trading, daily profits, and secure payments'>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { text-align: center; color: white; margin-bottom: 40px; animation: fadeInDown 1s; }
        .header h1 { font-size: 3.5em; margin-bottom: 15px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .header p { font-size: 1.3em; opacity: 0.95; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-bottom: 40px; }
        .feature { background: rgba(255,255,255,0.95); padding: 35px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s, box-shadow 0.3s; animation: fadeInUp 1s; }
        .feature:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.3); }
        .feature h3 { font-size: 1.8em; margin-bottom: 15px; color: #667eea; }
        .feature p { font-size: 1.1em; line-height: 1.6; color: #666; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 50px 0; }
        .stat { background: rgba(255,255,255,0.9); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15); animation: fadeInUp 1.2s; }
        .stat h4 { font-size: 2.5em; margin-bottom: 8px; color: #667eea; font-weight: bold; }
        .stat p { font-size: 1.1em; color: #666; }
        .cta { text-align: center; color: white; margin: 50px 0; animation: fadeInUp 1.4s; }
        .cta h2 { font-size: 2.5em; margin-bottom: 25px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .btn { display: inline-block; padding: 18px 40px; background: linear-gradient(45deg, #4CAF50, #45a049); color: white; text-decoration: none; border-radius: 50px; margin: 10px; font-weight: bold; font-size: 1.1em; transition: all 0.3s; box-shadow: 0 4px 15px rgba(76,175,80,0.3); }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(76,175,80,0.4); background: linear-gradient(45deg, #45a049, #4CAF50); }
        .btn-secondary { background: linear-gradient(45deg, #ff9800, #e68900); box-shadow: 0 4px 15px rgba(255,152,0,0.3); }
        .btn-secondary:hover { background: linear-gradient(45deg, #e68900, #ff9800); box-shadow: 0 6px 20px rgba(255,152,0,0.4); }
        .message { background: rgba(76,175,80,0.9); color: white; padding: 20px; border-radius: 10px; margin: 20px auto; max-width: 600px; text-align: center; animation: slideIn 0.5s; }
        .modal { display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); animation: fadeIn 0.3s; }
        .modal-content { background: white; margin: 5% auto; padding: 30px; border-radius: 15px; width: 90%; max-width: 500px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); animation: slideInUp 0.5s; }
        .close { color: #aaa; float: right; font-size: 28px; font-weight: bold; cursor: pointer; }
        .close:hover { color: #000; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: bold; color: #333; }
        .form-group input { width: 100%; padding: 12px; border: 2px solid #ddd; border-radius: 8px; font-size: 1em; transition: border-color 0.3s; }
        .form-group input:focus { outline: none; border-color: #667eea; }
        .footer { text-align: center; color: white; margin-top: 80px; padding: 40px 20px; opacity: 0.9; border-top: 1px solid rgba(255,255,255,0.2); }
        @keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes slideIn { from { transform: translateX(-20px); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideInUp { from { transform: translateY(50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <h1>🚀 CopyBloom FX</h1>
            <p>Professional Crypto Investment Platform - Trade Like the Pros</p>
        </div>";

if ($message) {
    echo "<div class='message'>$message</div>";
}

echo "
        <div class='features'>
            <div class='feature'>
                <h3>💰 Copy Trading</h3>
                <p>Copy successful traders automatically and earn consistent profits like professional investors</p>
            </div>
            <div class='feature'>
                <h3>📈 6 Rank Levels</h3>
                <p>Progress from Green Horn to Market Wizard with increasing daily profits and trading limits</p>
            </div>
            <div class='feature'>
                <h3>🔒 Secure Payments</h3>
                <p>Paystack integration ensures safe, fast deposits and withdrawals with live transaction monitoring</p>
            </div>
            <div class='feature'>
                <h3>🎯 Daily Profits</h3>
                <p>Earn reliable 5% daily returns on your investments with automated profit distribution</p>
            </div>
            <div class='feature'>
                <h3>👥 Referral System</h3>
                <p>Generate passive income by referring new users and earning bonuses on their investments</p>
            </div>
            <div class='feature'>
                <h3>📊 Real-time Analytics</h3>
                <p>Track your portfolio performance, profits, and trading history with detailed analytics dashboard</p>
            </div>
        </div>

        <div class='stats'>
            <div class='stat'>
                <h4>5%</h4>
                <p>Daily Returns</p>
            </div>
            <div class='stat'>
                <h4>6</h4>
                <p>Rank Levels</p>
            </div>
            <div class='stat'>
                <h4>24/7</h4>
                <p>Auto Trading</p>
            </div>
            <div class='stat'>
                <h4>100%</h4>
                <p>Secure Platform</p>
            </div>
        </div>

        <div class='cta'>
            <h2>🎯 Start Your Crypto Journey Today!</h2>
            <p>Join thousands of successful investors earning daily profits</p>
            <button class='btn' onclick='showRegisterModal()'>🚀 Get Started</button>
            <button class='btn btn-secondary' onclick='showLoginModal()'>🔐 Login</button>
        </div>

        <div class='footer'>
            <p>&copy; 2026 CopyBloom FX. All rights reserved.</p>
            <p>Powered by advanced blockchain technology | Secured by industry-leading encryption</p>
            <p>📍 Operating globally with trusted payment partners</p>
        </div>
    </div>

    <!-- Register Modal -->
    <div id='registerModal' class='modal'>
        <div class='modal-content'>
            <span class='close' onclick='closeModal(\"registerModal\")'>&times;</span>
            <h2 style='color: #667eea; margin-bottom: 25px;'>🚀 Create Account</h2>
            <form method='POST'>
                <input type='hidden' name='action' value='register'>
                <div class='form-group'>
                    <label>Full Name:</label>
                    <input type='text' name='name' required placeholder='Enter your full name'>
                </div>
                <div class='form-group'>
                    <label>Email Address:</label>
                    <input type='email' name='email' required placeholder='Enter your email'>
                </div>
                <div class='form-group'>
                    <label>Phone Number:</label>
                    <input type='tel' name='phone' placeholder='Enter your phone number'>
                </div>
                <div class='form-group'>
                    <label>Password:</label>
                    <input type='password' name='password' required placeholder='Create a strong password'>
                </div>
                <button type='submit' class='btn' style='width: 100%; margin-top: 20px;'>Create Account</button>
            </form>
        </div>
    </div>

    <!-- Login Modal -->
    <div id='loginModal' class='modal'>
        <div class='modal-content'>
            <span class='close' onclick='closeModal(\"loginModal\")'>&times;</span>
            <h2 style='color: #667eea; margin-bottom: 25px;'>🔐 Login</h2>
            <form method='POST'>
                <input type='hidden' name='action' value='login'>
                <div class='form-group'>
                    <label>Email Address:</label>
                    <input type='email' name='email' required placeholder='Enter your email'>
                </div>
                <div class='form-group'>
                    <label>Password:</label>
                    <input type='password' name='password' required placeholder='Enter your password'>
                </div>
                <button type='submit' class='btn' style='width: 100%; margin-top: 20px;'>Login</button>
            </form>
        </div>
    </div>

    <script>
        function showRegisterModal() {
            document.getElementById('registerModal').style.display = 'block';
        }
        
        function showLoginModal() {
            document.getElementById('loginModal').style.display = 'block';
        }
        
        function closeModal(modalId) {
            document.getElementById(modalId).style.display = 'none';
        }
        
        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target.className === 'modal') {
                event.target.style.display = 'none';
            }
        }
    </script>
</body>
</html>";
?>
