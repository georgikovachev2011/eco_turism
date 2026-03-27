document.addEventListener("DOMContentLoaded", () => {
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

    const minSlider = document.getElementById("minSlider");
    const maxSlider = document.getElementById("maxSlider");
    const priceValue = document.getElementById("priceValue");

    function updatePrice() {
        let min = parseInt(minSlider.value);
        let max = parseInt(maxSlider.value);

        if (min > max) {
            [min, max] = [max, min];
        }

        priceValue.textContent = `${min} lv - ${max} lv`;
    }

    if (minSlider && maxSlider && priceValue) {
        minSlider.addEventListener("input", updatePrice);
        maxSlider.addEventListener("input", updatePrice);
        updatePrice();
    }

    const heartButtons = document.querySelectorAll(".heart");

    heartButtons.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            event.stopPropagation();
            button.classList.toggle("active");
            button.textContent = button.classList.contains("active") ? "♥" : "♡";
        });
    });
});