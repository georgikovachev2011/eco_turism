document.addEventListener("DOMContentLoaded", () => {
    const burger = document.querySelector(".burger");
    const mobileMenu = document.querySelector(".mobile-menu");
    const closeMenu = document.querySelector(".close-menu");
    const cardsContainer = document.querySelector(".cards");

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

    if (cardsContainer) {
        cardsContainer.addEventListener("click", (event) => {
            const button = event.target.closest(".favorite");

            if (button) {
                event.preventDefault();
                event.stopPropagation();
                button.classList.toggle("active");
                button.textContent = button.classList.contains("active") ? "♥" : "♡";
            }
        });
    }

    fetch("/homepage_response/")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Failed to load homepage data.");
            }
            return response.json();
        })
        .then((data) => {
            if (!cardsContainer) return;

            cardsContainer.innerHTML = "";

            data.forEach((lodge) => {
                const card = document.createElement("a");
                card.href = `/destination/${lodge.id}/`;
                card.className = "card";

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

                cardsContainer.appendChild(card);
            });
        })
        .catch((error) => {
            console.error(error);
            if (cardsContainer) {
                cardsContainer.innerHTML = `<p>Unable to load destinations right now.</p>`;
            }
        });
});