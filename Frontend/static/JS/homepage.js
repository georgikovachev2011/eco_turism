fetch("/homepage_response/")
.then(response => response.json())
.then(data => {
    console.log(data)
})

document.addEventListener("DOMContentLoaded", () => {
    const burger = document.querySelector(".burger");
    const mobileMenu = document.querySelector(".mobile-menu");
    const closeMenu = document.querySelector(".close-menu");
    const favoriteButtons = document.querySelectorAll(".favorite");

    if (burger && mobileMenu) {
        burger.addEventListener("click", () => {
            mobileMenu.classList.add("active");
        });
    }

    if (closeMenu && mobileMenu) {
        closeMenu.addEventListener("click", () => {
            mobileMenu.classList.remove("active");
        });
    }

    favoriteButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            event.stopPropagation();
            button.classList.toggle("active");
            button.textContent = button.classList.contains("active") ? "♥" : "♡";
        });
    });
});

if(localStorage.getItem("authUser")){
    document.getElementById("login-button").remove()
}