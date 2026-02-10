<?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['user_email'])) {
    header('Location: /');
    exit();
}

// Handle logout
if (isset($_POST['logout'])) {
    session_destroy();
    header('Location: /');
    exit();
}

$user_email = $_SESSION['user_email'];
$user_name = $_SESSION['user_name'] ?? 'User';
?>
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - CopyBloom FX</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; color: #333; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .header-content { display: flex; justify-content: space-between; align-items: center; }
        .user-info h1 { color: #667eea; font-size: 2em; }
        .user-info p { color: #666; }
        .logout-btn { background: #f44336; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .stat-card { background: white; padding: 25px; border-radius: 10px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .stat-card h3 { color: #667eea; font-size: 2em; margin-bottom: 10px; }
        .actions { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .action-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .action-card h3 { color: #667eea; margin-bottom: 15px; }
        .btn { display: inline-block; padding: 12px 25px; background: #4CAF50; color: white; text-decoration: none; border-radius: 5px; margin: 5px; }
        .btn-secondary { background: #ff9800; }
        .btn-danger { background: #f44336; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-content">
                <div class="user-info">
                    <h1>Welcome, <?php echo htmlspecialchars($user_name); ?>!</h1>
                    <p>Email: <?php echo htmlspecialchars($user_email); ?></p>
                </div>
                <form method="POST">
                    <button type="submit" name="logout" class="logout-btn">Logout</button>
                </form>
            </div>
        </div>

        <div class="stats">
            <div class="stat-card">
                <h3>$0.00</h3>
                <p>Total Balance</p>
            </div>
            <div class="stat-card">
                <h3>$0.00</h3>
                <p>Available Balance</p>
            </div>
            <div class="stat-card">
                <h3>$0.00</h3>
                <p>Total Profits</p>
            </div>
            <div class="stat-card">
                <h3>0</h3>
                <p>Active Trades</p>
            </div>
        </div>

        <div class="actions">
            <div class="action-card">
                <h3>💰 Make Deposit</h3>
                <p>Fund your account to start trading and earning daily profits.</p>
                <a href="#" class="btn">Deposit Now</a>
            </div>
            <div class="action-card">
                <h3>📈 Copy Trading</h3>
                <p>Copy successful traders automatically and earn like the pros.</p>
                <a href="#" class="btn btn-secondary">Start Copy Trading</a>
            </div>
            <div class="action-card">
                <h3>💸 Withdraw</h3>
                <p>Withdraw your profits securely to your bank account.</p>
                <a href="#" class="btn btn-danger">Withdraw Funds</a>
            </div>
        </div>
    </div>
</body>
</html>
