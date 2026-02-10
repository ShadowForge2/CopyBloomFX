// Risk Warning Ticker JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Risk warning messages
    const riskMessages = [
        '⚠️ Risk Warning: Cryptocurrency trading involves significant risk and may result in the loss of all invested capital.',
        '⚠️ Copy Trading Notice: Copy trading does not guarantee profits. Copied traders\' strategies may change or fail at any time.',
        '⚠️ Disclaimer: This platform does not provide financial or investment advice. All trading decisions are made at your own risk.',
        '⚠️ High Volatility Alert: Digital asset prices are highly volatile. Past performance does not guarantee future results.',
        '⚠️ Capital Risk: Only invest funds you can afford to lose. You are fully responsible for all trades executed on this platform.'
    ];

    // Create ticker container
    function createTicker() {
        // Check if ticker already exists
        if (document.getElementById('riskTicker')) {
            return;
        }

        // Create ticker HTML
        const tickerHTML = `
            <div id="riskTicker" class="risk-ticker-container">
                <div class="risk-ticker-wrapper">
                    <div class="risk-ticker-content" id="tickerContent">
                        <!-- Messages will be inserted here -->
                    </div>
                </div>
            </div>
        `;

        // Insert ticker at the end of body
        document.body.insertAdjacentHTML('beforeend', tickerHTML);

        // Populate ticker content
        populateTicker();
    }

    // Populate ticker with messages
    function populateTicker() {
        const tickerContent = document.getElementById('tickerContent');
        if (!tickerContent) return;

        // Create two sets of messages for seamless looping
        const allMessages = [...riskMessages, ...riskMessages];
        
        let tickerHTML = '';
        allMessages.forEach(message => {
            tickerHTML += `<span class="risk-ticker-item">
                <span class="warning-icon">⚠️</span>
                ${message}
            </span>`;
        });

        tickerContent.innerHTML = tickerHTML;
    }

    // Optimize animation performance
    function optimizeAnimation() {
        const tickerContent = document.getElementById('tickerContent');
        if (tickerContent) {
            // Use GPU acceleration
            tickerContent.style.transform = 'translateZ(0)';
            tickerContent.style.willChange = 'transform';
        }
    }

    // Handle visibility changes to pause/resume animation
    function handleVisibilityChange() {
        const tickerContent = document.getElementById('tickerContent');
        if (!tickerContent) return;

        if (document.hidden) {
            // Pause animation when tab is not visible
            tickerContent.style.animationPlayState = 'paused';
        } else {
            // Resume animation when tab is visible
            tickerContent.style.animationPlayState = 'running';
        }
    }

    // Initialize ticker
    createTicker();
    optimizeAnimation();

    // Add visibility change listener
    document.addEventListener('visibilitychange', handleVisibilityChange);

    // Handle window resize for responsive behavior
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(function() {
            optimizeAnimation();
        }, 250);
    });

    // Ensure ticker stays on top of other content
    function ensureTickerVisibility() {
        const ticker = document.getElementById('riskTicker');
        if (ticker) {
            ticker.style.zIndex = '9999';
        }
    }

    // Periodically check ticker visibility
    setInterval(ensureTickerVisibility, 5000);
});
