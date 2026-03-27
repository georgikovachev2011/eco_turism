const cardNumber = document.getElementById("cardNumber");
const expiry = document.getElementById("expiry");
const cvv = document.getElementById("cvv");

cardNumber.addEventListener("input", (e) => {
    let value = e.target.value.replace(/\D/g, "");
    value = value.replace(/(.{4})/g, "$1 ").trim();
    e.target.value = value;
});

expiry.addEventListener("input", (e) => {
    let value = e.target.value.replace(/\D/g, "");
    if (value.length >= 3) {
        value = value.slice(0,2) + "/" + value.slice(2,4);
    }
    e.target.value = value;
});

cvv.addEventListener("input", (e) => {
    e.target.value = e.target.value.replace(/\D/g, "");
});

document.getElementById("payment-form").addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Payment submitted!");
});