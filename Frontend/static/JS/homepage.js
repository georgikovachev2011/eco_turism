const burger = document.querySelector(".burger");
const mobileMenu = document.querySelector(".mobile-menu");
const closeMenu = document.querySelector(".close-menu");


fetch("/homepage_response/")
.then(response => response.json())
.then(data => {
    const container = document.querySelector(".cards");
    data.forEach(lodge => {
  const card = document.createElement("a");
  card.href = `/destination/${lodge.id}`;
  card.classList.add("card");

  card.innerHTML = `
    <div class="card-image">
        <img src="${lodge.image}" alt="${lodge.name}">
        <span class="badge">Featured</span>
        <button class="favorite" type="button">♡</button>
    </div>
    <div class="card-content">
        <h3>${lodge.name}</h3>
        <p class="location">📍 ${lodge.location}</p>
        <p class="description">${lodge.short_description}</p>
        <p class="rating">⭐ <strong>${lodge.rating}</strong> (${lodge.reviews} reviews)</p>
        <div class="card-footer">
            <span>👥 Up to ${lodge.num_of_guests} guests</span>
            <span class="price">${lodge.dollars_per_night} lv<span>/night</span></span>
        </div>
    </div>
  `;

  container.appendChild(card);
});
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