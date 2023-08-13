// static/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById("submit-button");
    if (submitButton) {
        submitButton.addEventListener("click", function () {
            const form = document.getElementById("service-request-form");
            if (form) {
                form.submit();
            }
        });
    }
});
