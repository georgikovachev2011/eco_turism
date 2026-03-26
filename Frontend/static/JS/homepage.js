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