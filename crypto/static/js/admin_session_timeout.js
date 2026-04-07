// Admin Session Timeout Manager
class AdminSessionManager {
    constructor() {
        this.timeoutDuration = 60 * 1000; // 1 minute in milliseconds
        this.warningDuration = 10 * 1000; // Show warning at 10 seconds
        this.timeoutId = null;
        this.warningTimeoutId = null;
        this.init();
    }

    init() {
        // Start tracking when page loads
        this.startSessionTracking();
        
        // Track user activity
        this.trackActivity();
        
        // Show session timer
        this.showSessionTimer();
    }

    startSessionTracking() {
        // Clear existing timeouts
        this.clearTimeouts();
        
        // Start warning timeout
        this.warningTimeoutId = setTimeout(() => {
            this.showWarning();
        }, this.timeoutDuration - this.warningDuration);
        
        // Start session timeout
        this.timeoutId = setTimeout(() => {
            this.handleTimeout();
        }, this.timeoutDuration);
    }

    trackActivity() {
        // Track user activity to reset timer
        const events = ['mousedown', 'mousemove', 'keypress', 'scroll', 'click', 'touchstart'];
        
        events.forEach(event => {
            document.addEventListener(event, () => {
                this.resetTimer();
            });
        });
    }

    resetTimer() {
        // Clear existing timeouts
        this.clearTimeouts();
        
        // Start new timer
        this.startSessionTracking();
        
        // Update timer display
        this.updateTimerDisplay(this.timeoutDuration);
    }

    clearTimeouts() {
        if (this.timeoutId) {
            clearTimeout(this.timeoutId);
        }
        if (this.warningTimeoutId) {
            clearTimeout(this.warningTimeoutId);
        }
    }

    showSessionTimer() {
        // Create or update timer display
        let timerDiv = document.getElementById('admin-session-timer');
        
        if (!timerDiv) {
            timerDiv = document.createElement('div');
            timerDiv.id = 'admin-session-timer';
            timerDiv.style.cssText = `
                position: fixed;
                top: 10px;
                right: 10px;
                background: #ff6b6b;
                color: white;
                padding: 8px 12px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
                z-index: 9999;
                box-shadow: 0 2px 4px rgba(0,0,0,0.2);
            `;
            document.body.appendChild(timerDiv);
        }
        
        this.updateTimerDisplay(this.timeoutDuration);
    }

    updateTimerDisplay(remainingTime) {
        const timerDiv = document.getElementById('admin-session-timer');
        if (timerDiv) {
            const seconds = Math.ceil(remainingTime / 1000);
            timerDiv.textContent = `Admin Session: ${seconds}s`;
            
            // Change color based on time remaining
            if (remainingTime < 10000) { // Less than 10 seconds
                timerDiv.style.background = '#dc3545'; // Red
            } else if (remainingTime < 30000) { // Less than 30 seconds
                timerDiv.style.background = '#ffc107'; // Yellow
            } else {
                timerDiv.style.background = '#28a745'; // Green
            }
        }
    }

    showWarning() {
        // Show warning modal
        const warningModal = document.createElement('div');
        warningModal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10000;
        `;
        
        warningModal.innerHTML = `
            <div style="background: white; padding: 30px; border-radius: 8px; max-width: 400px; text-align: center;">
                <h3 style="color: #dc3545; margin-bottom: 15px;">⚠️ Session Expiring Soon!</h3>
                <p style="margin-bottom: 20px;">Your admin session will expire in 10 seconds. Please save your work.</p>
                <button onclick="this.parentElement.parentElement.remove()" style="background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">
                    I Understand
                </button>
            </div>
        `;
        
        document.body.appendChild(warningModal);
        
        // Auto-remove warning after 8 seconds
        setTimeout(() => {
            if (warningModal.parentNode) {
                warningModal.remove();
            }
        }, 8000);
    }

    handleTimeout() {
        // Show timeout message and redirect
        const timeoutModal = document.createElement('div');
        timeoutModal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.9);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10001;
        `;
        
        timeoutModal.innerHTML = `
            <div style="background: white; padding: 30px; border-radius: 8px; max-width: 400px; text-align: center;">
                <h3 style="color: #dc3545; margin-bottom: 15px;">🔒 Session Expired</h3>
                <p style="margin-bottom: 20px;">Your admin session has expired. You will be redirected to login.</p>
                <div style="color: #6c757d; font-size: 14px;">Redirecting in <span id="countdown">5</span> seconds...</div>
            </div>
        `;
        
        document.body.appendChild(timeoutModal);
        
        // Countdown and redirect
        let countdown = 5;
        const countdownInterval = setInterval(() => {
            countdown--;
            const countdownSpan = document.getElementById('countdown');
            if (countdownSpan) {
                countdownSpan.textContent = countdown;
            }
            
            if (countdown <= 0) {
                clearInterval(countdownInterval);
                window.location.href = '/admin/login/';
            }
        }, 1000);
    }
}

// Initialize session manager when page loads
document.addEventListener('DOMContentLoaded', () => {
    // Only run on admin pages
    if (window.location.pathname.startsWith('/admin/')) {
        new AdminSessionManager();
    }
});
