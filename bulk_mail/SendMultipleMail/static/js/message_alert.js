// Function to hide messages smoothly after 5 seconds
setTimeout(function() {
    var messages = document.querySelectorAll('.alert');
    messages.forEach(function(message) {
        message.style.opacity = '1';
        setTimeout(function() {
            message.style.display = 'none';
        }, 1000); // Delay hiding the message after opacity transition
    });
}, 5000); // 5000 milliseconds = 5 seconds