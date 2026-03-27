const resetForm = document.getElementById("resetForm");

function getTokenFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get("token");
}

resetForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const urlToken = getTokenFromURL();
    const savedToken = localStorage.getItem("resetToken");
    const newPassword = document.getElementById("newPassword").value.trim();
    const confirmPassword = document.getElementById("confirmPassword").value.trim();

    if (!urlToken || urlToken !== savedToken) {
        alert("Invalid or expired reset link.");
        return;
    }

    if (!newPassword || !confirmPassword) {
        alert("Please fill in all fields.");
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

    window.location.href = "sign-in.html";
});