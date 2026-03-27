document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("resetForm");
    const newPasswordInput = document.getElementById("newPassword");
    const confirmPasswordInput = document.getElementById("confirmPassword");

    if (!form || !newPasswordInput || !confirmPasswordInput) {
        return;
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const newPassword = newPasswordInput.value.trim();
        const confirmPassword = confirmPasswordInput.value.trim();

        if (!newPassword || !confirmPassword) {
            alert("Please fill in both password fields.");
            return;
        }

        if (newPassword.length < 6) {
            alert("Password must be at least 6 characters long.");
            return;
        }

        if (newPassword !== confirmPassword) {
            alert("Passwords do not match.");
            return;
        }

        localStorage.setItem("userPassword", newPassword);
        localStorage.removeItem("resetToken");

        alert("Your password has been reset successfully.");
        window.location.href = "/sign-in";
    });
});