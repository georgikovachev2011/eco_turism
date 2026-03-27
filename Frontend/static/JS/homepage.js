const burger = document.querySelector(".burger");
const mobileMenu = document.querySelector(".mobile-menu");
const closeMenu = document.querySelector(".close-menu");


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

const favoriteButtons = document.querySelectorAll(".favorite");

favoriteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        event.stopPropagation();
        button.classList.toggle("active");
        button.textContent = button.classList.contains("active") ? "♥" : "♡";
    });
});