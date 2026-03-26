const signupForm = document.getElementById("signupForm");
const signinForm = document.getElementById("signinForm");

if (signupForm) {
  signupForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("signupUsername").value.trim();
    const email = document.getElementById("signupEmail").value.trim();
    const password = document.getElementById("signupPassword").value;
    const confirmPassword = document.getElementById("signupConfirmPassword").value;
    const message = document.getElementById("signupMessage");

    message.textContent = "";
    message.className = "message";

    if (password.length < 6) {
      message.textContent = "Password must be at least 6 characters.";
      message.classList.add("error");
      return;
    }

    if (password !== confirmPassword) {
      message.textContent = "Passwords do not match.";
      message.classList.add("error");
      return;
    }

    const user = {
      username,
      email,
      password
    };

    localStorage.setItem("authUser", JSON.stringify(user));

    message.textContent = "Registration successful. Redirecting to login...";
    message.classList.add("success");

    setTimeout(() => {
      window.location.href = "signin.html";
    }, 1500);
  });
}

if (signinForm) {
  signinForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("signinUsername").value.trim();
    const password = document.getElementById("signinPassword").value;
    const message = document.getElementById("signinMessage");

    message.textContent = "";
    message.className = "message";

    const savedUser = JSON.parse(localStorage.getItem("authUser"));

    if (!savedUser) {
      message.textContent = "No account found. Please register first.";
      message.classList.add("error");
      return;
    }

    if (username === savedUser.username && password === savedUser.password) {
      message.textContent = "Login successful.";
      message.classList.add("success");
    } else {
      message.textContent = "Invalid username or password.";
      message.classList.add("error");
    }
  });
}