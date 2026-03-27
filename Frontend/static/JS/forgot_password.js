const form = document.querySelector(".forgot-box");
const emailInput = document.getElementById("email");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const email = emailInput.value.trim();

    if (!email) {
        alert("Please enter your email address.");
        return;
    }

    const token = Math.random().toString(36).substring(2) + Date.now().toString(36);

    localStorage.setItem("resetToken", token);
    localStorage.setItem("resetEmail", email);

    window.location.href = `/email_sent?token=${token}`;
});