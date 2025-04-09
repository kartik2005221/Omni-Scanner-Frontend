// Function to dismiss the warning when clicked
function dismissWarning() {
    const warning = document.getElementById('sudo-warning');
    if (warning) {
        warning.style.display = 'none';
    }
}

// Automatically dismiss the warning after 5 seconds
setTimeout(() => {
    dismissWarning();
}, 5000);