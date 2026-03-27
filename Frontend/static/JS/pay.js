document.addEventListener("DOMContentLoaded", () => {
    const cardNumber = document.getElementById("cardNumber");
    const expiry = document.getElementById("expiry");
    const cvv = document.getElementById("cvv");
    const paymentForm = document.getElementById("payment-form");

    if (cardNumber) {
        cardNumber.addEventListener("input", (e) => {
            let value = e.target.value.replace(/\D/g, "");
            value = value.replace(/(.{4})/g, "$1 ").trim();
            e.target.value = value;
        });
    }

    if (expiry) {
        expiry.addEventListener("input", (e) => {
            let value = e.target.value.replace(/\D/g, "");
            if (value.length >= 3) {
                value = value.slice(0, 2) + "/" + value.slice(2, 4);
            }
            e.target.value = value;
        });
    }

    if (cvv) {
        cvv.addEventListener("input", (e) => {
            e.target.value = e.target.value.replace(/\D/g, "");
        });
    }

    if (paymentForm) {
        paymentForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Payment submitted!");
        });
    }
});