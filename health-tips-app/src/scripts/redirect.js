document.addEventListener('DOMContentLoaded', function() {
    const redirectButton = document.getElementById('redirect-to-login');

    if (redirectButton) {
        redirectButton.addEventListener('click', function() {
            window.location.href = 'login.html';
        });
    }
});