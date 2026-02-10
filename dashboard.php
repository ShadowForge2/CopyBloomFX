<?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['user_email'])) {
    header('Location: /');
    exit();
}

// Get user data
$user_email = $_SESSION['user_email'];
$user_name = $_SESSION['user_name'] ?? 'User';

// Handle logout
if ($_POST['action'] == 'logout') {
    session_destroy();
    header('Location: /');
    exit();
}

echo "<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - CopyBloom FX</title>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { background: rgba(255,255,255,0.95); padding: 20px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        .header-content { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
        .user-info h1 { color: #667eea; font-size: 2em; margin-bottom: 5px; }
        .user-info p { color: #666; font-size: 1.1em; }
        .logout-btn { background: linear-gradient(45deg, #f44336, #d32f2f); color: white; padding: 12px 25px; border: none; border-radius: 25px; cursor: pointer; font-weight: bold; transition: all 0.3s; }
        .logout-btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(244,67,54,0.3); }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .stat-card { background: rgba(255,255,255,0.95); padding: 25px; border-radius: 15px; text-align: center; box-shadow: 0 8px 25px rgba(0,0,0,0.15); transition: transform 0.3s; }
        .stat-card:hover { transform: translateY(-5px); }
        .stat-card h3 { color: #667eea; font-size: 2.5em; margin-bottom: 10px; }
        .stat-card p { color: #666; font-size: 1.1em; }
        .actions-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .action-card { background: rgba(255,255,255,0.95); padding: 30px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.15); }
        .action-card h3 { color: #667eea; font-size: 1.5em; margin-bottom: 15px; }
        .action-card p { color: #666; margin-bottom: 20px; line-height: 1.6; }
        .btn { display: inline-block; padding: 12px 25px; background: linear-gradient(45deg, #4CAF50, #45a049); color: white; text-decoration: none; border-radius: 25px; font-weight: bold; transition: all 0.3s; }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(76,175,80,0.3); }
        .btn-secondary { background: linear-gradient(45deg, #ff9800, #e68900); }
        .btn-secondary:hover { box-shadow: 0 5px 15px rgba(255,152,0,0.3); }
        .btn-danger { background: linear-gradient(45deg, #f44336, #d32f2f); }
        .btn-danger:hover { box-shadow: 0 5px 15px rgba(244,67,54,0.3); }
        .rank-badge { background: linear-gradient(45deg, #9c27b0, #7b1fa2); color: white; padding: 8px 20px; border-radius: 20px; font-weight: bold; display: inline-block; margin-top: 10px; }
        .recent-activity { background: rgba(255,255,255,0.95); padding: 30px; border-radius: 15px; box-shadow: 0 8px 25px rgba(0,0,0,0.15); }
        .recent-activity h3 { color: #667eea; font-size: 1.5em; margin-bottom: 20px; }
        .activity-item { background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #667eea; }
        .activity-item p { color: #666; margin: 0; }
        .activity-item small { color: #999; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='header'>
            <div class='header-content'>
                <div class='user-info'>
                    <h1>👋 Welcome, $user_name!</h1>
                    <p>📧 $user_email | <span class='rank-badge'>🏆 Green Horn</span></p>
                </div>
                <form method='POST' style='margin: 0;'>
                    <input type='hidden' name='action' value='logout'>
                    <button type='submit' class='logout-btn'>🚪 Logout</button>
                </form>
            </div>
        </div>

        <div class='stats-grid'>
            <div class='stat-card'>
                <h3>\$0.00</h3>
                <p>Total Balance</p>
            </div>
            <div class='stat-card'>
                <h3>\$0.00</h3>
                <p>Available Balance</p>
            </div>
            <div class='stat-card'>
                <h3>\$0.00</h3>
                <p>Total Profits</p>
            </div>
            <div class='stat-card'>
                <h3>0</h3>
                <p>Active Trades</p>
            </div>
        </div>

        <div class='actions-grid'>
            <div class='action-card'>
                <h3>💰 Make Deposit</h3>
                <p>Fund your account to start trading and earning daily profits. Multiple payment methods available.</p>
                <a href='/deposit.php' class='btn'>💳 Deposit Now</a>
            </div>
            <div class='action-card'>
                <h3>📈 Copy Trading</h3>
                <p>Copy successful traders automatically and earn like the pros. Choose from expert traders.</p>
                <a href='/copytrade.php' class='btn btn-secondary'>🔄 Start Copy Trading</a>
            </div>
            <div class='action-card'>
                <h3>💸 Withdraw</h3>
                <p>Withdraw your profits securely to your bank account or cryptocurrency wallet.</p>
                <a href='/withdraw.php' class='btn btn-danger'>💳 Withdraw Funds</a>
            </div>
        </div>

        <div class='recent-activity'>
            <h3>📊 Recent Activity</h3>
            <div class='activity-item'>
                <p><strong>Welcome to CopyBloom FX!</strong></p>
                <small>Just now</small>
            </div>
            <div class='activity-item'>
                <p><strong>Account created successfully</strong></p>
                <small>Just now</small>
            </div>
            <div class='activity-item'>
                <p><strong>Ready to start your crypto journey</strong></p>
                <small>Just now</small>
            </div>
        </div>
    </div>
</body>
</html>";
?>
