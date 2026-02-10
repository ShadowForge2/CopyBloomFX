<?php
/**
 * Database Migration Script for InfinityFree
 * This script will run Django migrations
 */

echo "<!DOCTYPE html>
<html>
<head>
    <title>Database Migration - Crypto Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        .status { padding: 15px; margin: 10px 0; border-radius: 5px; }
        .success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .info { background: #d1ecf1; color: #0c5460; border: 1px solid #bee5eb; }
        .warning { background: #fff3cd; color: #856404; border: 1px solid #ffeaa7; }
        .error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .btn { display: inline-block; padding: 10px 20px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; margin: 5px; }
        .btn:hover { background: #0056b3; }
        .btn-success { background: #28a745; }
        .btn-success:hover { background: #1e7e34; }
    </style>
</head>
<body>
    <div class='container'>
        <h1>🗄️ Database Migration</h1>
        
        <div class='status info'>
            <h3>📋 Migration Status</h3>
            <p>This page will help you set up your database tables.</p>
        </div>";

// Check if form is submitted
if ($_POST['action'] == 'migrate') {
    echo "<div class='status success'>";
    echo "<h3>✅ Migration Instructions</h3>";
    echo "<p>Since InfinityFree doesn't allow direct shell access, you need to:</p>";
    echo "<ol>";
    echo "<li>Go to InfinityFree Control Panel</li>";
    echo "<li>Click 'MySQL Database'</li>";
    echo "<li>Click 'phpMyAdmin'</li>";
    echo "<li>Select your database</li>";
    echo "<li>Click 'Import'</li>";
    echo "<li>Upload the SQL file from your local Django project</li>";
    echo "</ol>";
    echo "</div>";
    
    echo "<div class='status info'>";
    echo "<h3>🔧 Alternative: Manual Table Creation</h3>";
    echo "<p>You can create tables manually using this SQL:</p>";
    echo "<pre style='background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto;'>";
    echo "-- Create Users Table
CREATE TABLE IF NOT EXISTS crypto_customuser (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    is_active BOOLEAN DEFAULT TRUE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_login DATETIME,
    phone VARCHAR(20),
    role VARCHAR(20) DEFAULT 'user',
    is_banned BOOLEAN DEFAULT FALSE,
    is_flagged BOOLEAN DEFAULT FALSE,
    referral_code VARCHAR(16) UNIQUE,
    referred_by_id INT
);

-- Create Profile Table
CREATE TABLE IF NOT EXISTS crypto_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE NOT NULL,
    rank_id INT,
    locked_balance DECIMAL(18,2) DEFAULT 0.00,
    withdrawable_balance DECIMAL(18,2) DEFAULT 0.00,
    profile_picture TEXT,
    referral_code VARCHAR(16) UNIQUE,
    total_referrals INT DEFAULT 0,
    valid_referrals INT DEFAULT 0,
    referral_earnings DECIMAL(18,2) DEFAULT 0.00,
    last_withdrawal_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES crypto_customuser(id)
);

-- Create Ranks Table
CREATE TABLE IF NOT EXISTS crypto_rank (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    min_balance DECIMAL(18,2) NOT NULL,
    daily_profit_pct DECIMAL(5,2) NOT NULL,
    copy_trades_limit INT NOT NULL,
    description TEXT
);

-- Insert Default Ranks
INSERT INTO crypto_rank (name, min_balance, daily_profit_pct, copy_trades_limit, description) VALUES
('Green Horn', 50.00, 5.00, 1, 'Beginner level'),
('Student Form', 100.00, 5.00, 2, 'Learning level'),
('Market Maven', 150.00, 5.00, 3, 'Intermediate level'),
('Gunslinger', 500.00, 5.00, 4, 'Advanced level'),
('Whale', 1500.00, 5.00, 5, 'Expert level'),
('Market Wizard', 5000.00, 5.00, 6, 'Master level');

-- Create Deposits Table
CREATE TABLE IF NOT EXISTS crypto_deposit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(18,2) NOT NULL,
    network VARCHAR(32) NOT NULL,
    wallet_address VARCHAR(128),
    status VARCHAR(16) DEFAULT 'pending',
    expires_at DATETIME,
    approved_at DATETIME,
    referrer_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES crypto_customuser(id)
);

-- Create CopyTrades Table
CREATE TABLE IF NOT EXISTS crypto_copytrade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    pair VARCHAR(20) NOT NULL,
    action VARCHAR(10) NOT NULL,
    amount DECIMAL(18,2) NOT NULL,
    profit DECIMAL(18,2) DEFAULT 0.00,
    status VARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES crypto_customuser(id)
);";
    echo "</pre>";
    echo "</div>";
    
    echo "<div class='status success'>";
    echo "<h3>✅ Next Steps</h3>";
    echo "<p>After creating tables:</p>";
    echo "<ol>";
    echo "<li><a href='/admin/' class='btn'>🔐 Go to Admin Panel</a></li>";
    echo "<li><a href='/' class='btn btn-success'>🏠 Visit Your Site</a></li>";
    echo "</ol>";
    echo "</div>";
} else {
    echo "<div class='status warning'>";
    echo "<h3>⚠️ Database Setup Required</h3>";
    echo "<p>Your database tables need to be created before the platform can work.</p>";
    echo "</div>";
    
    echo "<form method='post'>";
    echo "<input type='hidden' name='action' value='migrate'>";
    echo "<button type='submit' class='btn btn-success'>🚀 Start Database Setup</button>";
    echo "</form>";
}

echo "
    </div>
</body>
</html>";
?>
