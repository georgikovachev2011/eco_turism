document.addEventListener("DOMContentLoaded", () => {
    const signinForm = document.getElementById("signinForm");
    const signinUsername = document.getElementById("signinUsername");
    const signinPassword = document.getElementById("signinPassword");
    const rememberMe = document.getElementById("rememberMe");
    const signinMessage = document.getElementById("signinMessage");

    if (!signinForm || !signinUsername || !signinPassword || !signinMessage) {
        return;
    }

    signinForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = signinUsername.value.trim();
        const password = signinPassword.value.trim();

        const savedUsername = localStorage.getItem("registeredUsername");
        const savedPassword =
            localStorage.getItem("userPassword") ||
            localStorage.getItem("registeredPassword");

        signinMessage.classList.remove("success", "error");

        if (!username || !password) {
            signinMessage.textContent = "Please fill in all fields.";
            signinMessage.classList.add("error");
            return;
        }

        if (!savedUsername || !savedPassword) {
            signinMessage.textContent = "No account found. Please register first.";
            signinMessage.classList.add("error");
            return;
        }

        if (username === savedUsername && password === savedPassword) {
            if (rememberMe && rememberMe.checked) {
                localStorage.setItem("rememberedUser", username);
            } else {
                localStorage.removeItem("rememberedUser");
            }

            signinMessage.textContent = "Login successful.";
            signinMessage.classList.add("success");

            setTimeout(() => {
                window.location.href = "homepage.js";
            }, 800);
        } else {
            signinMessage.textContent = "Invalid username or password.";
            signinMessage.classList.add("error");
        }
    });

    const rememberedUser = localStorage.getItem("rememberedUser");
    if (rememberedUser) {
        signinUsername.value = rememberedUser;
        if (rememberMe) {
            rememberMe.checked = true;
        }
    }
});