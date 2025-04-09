
document.addEventListener('DOMContentLoaded', () => {
    const copyButtons = document.querySelectorAll('button');

    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const command = button.previousElementSibling.textContent.trim(); // Get the text to copy
            navigator.clipboard.writeText(command).then(() => {
                // Provide feedback to the user
                button.textContent = 'Copied!';
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000); // Reset button text after 2 seconds
            }).catch(err => {
                console.error('Failed to copy text: ', err);
            });
        });
    });
});
