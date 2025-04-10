// old javascript code, dont work in external ip, only in https, and localhost
//
// document.addEventListener("DOMContentLoaded", () => {
//     const copyButtons = document.querySelectorAll("button[data-copy]");
//
//     copyButtons.forEach(button => {
//         button.addEventListener("click", () => {
//             const targetId = button.getAttribute("data-copy");
//             const targetElement = document.getElementById(targetId);
//
//             if (targetElement) {
//                 const textToCopy = targetElement.textContent;
//
//                 navigator.clipboard.writeText(textToCopy).then(() => {
//                     button.textContent = "Copied!";
//                     setTimeout(() => {
//                         button.textContent = "Copy";
//                     }, 2000);
//                 }).catch(err => {
//                     console.error("Failed to copy text: ", err);
//                 });
//             }
//         });
//     });
// });


document.addEventListener("DOMContentLoaded", () => {
    const copyButtons = document.querySelectorAll("button[data-copy]");

    copyButtons.forEach(button => {
        button.addEventListener("click", () => {
            const targetId = button.getAttribute("data-copy");
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const textToCopy = targetElement.textContent;

                if (navigator.clipboard && window.isSecureContext) {
                    // Use navigator.clipboard if available
                    navigator.clipboard.writeText(textToCopy).then(() => {
                        button.textContent = "Copied!";
                        setTimeout(() => {
                            button.textContent = "Copy";
                        }, 2000);
                    }).catch(err => {
                        console.error("Failed to copy text: ", err);
                    });
                } else {
                    // Fallback for insecure contexts
                    const textArea = document.createElement("textarea");
                    textArea.value = textToCopy;
                    textArea.style.position = "fixed"; // Prevent scrolling to bottom
                    textArea.style.opacity = "0";
                    document.body.appendChild(textArea);
                    textArea.focus();
                    textArea.select();

                    try {
                        document.execCommand("copy");
                        button.textContent = "Copied!";
                        setTimeout(() => {
                            button.textContent = "Copy";
                        }, 2000);
                    } catch (err) {
                        console.error("Fallback: Failed to copy text: ", err);
                    }

                    document.body.removeChild(textArea);
                }
            }
        });
    });
});