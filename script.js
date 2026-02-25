/**
 * Auto-Run script for VS Code
 * This script clicks the "Run" button in the AI chat panel when it's enabled.
 * Designed to be loaded via APC Customize UI++ or Custom CSS and JS Loader extensions.
 */

(function () {
    console.log("Auto-Run Script Loaded");

    const CLICK_INTERVAL_MS = 1000; // Check every second
    
    // Function to check and click the button
    function checkAndClickButton() {
        const buttons = document.querySelectorAll('button');
        
        for (const btn of buttons) {
            // Check if the button contains the required text and is NOT disabled
            if (btn.textContent.includes('Run') && 
                btn.textContent.includes('Alt+⏎') && 
                !btn.disabled &&
                // We're looking for the specific button class mentioned in button-info.txt
                btn.classList.contains('bg-primary') &&
                btn.classList.contains('text-primary-foreground')) {
                
                console.log("Auto-Run Script: Found active Run button! Clicking...", btn);
                btn.click();
                
                // Break out of the loop after clicking to avoid clicking multiple times in one tick
                break; 
            }
        }
    }

    // Start the polling loop
    setInterval(checkAndClickButton, CLICK_INTERVAL_MS);

    // Alternative approach using MutationObserver (Uncomment if setInterval is too slow/resource intensive)
    /*
    const observer = new MutationObserver((mutations) => {
        // We could optimize this by only checking when relevant nodes are added/modified
        checkAndClickButton();
    });
    
    // Observe the entire document for changes
    observer.observe(document.body, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['disabled', 'class'] // Watch for disabled attribute changes
    });
    */
})();
