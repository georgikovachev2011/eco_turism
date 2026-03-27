const minSlider = document.getElementById("minSlider");
const maxSlider = document.getElementById("maxSlider");
const priceValue = document.getElementById("priceValue");

const MAX = 200;

function updateSliders() {
  let min = parseInt(minSlider.value);
  let max = parseInt(maxSlider.value);

  // Prevent crossing
  if (min > max) {
    minSlider.value = max;
    min = max;
  }

  if (max < min) {
    maxSlider.value = min;
    max = min;
  }

  // Update text
  priceValue.textContent = `$${min} - $${max}`;

  // Convert to %
  const minPercent = (min / MAX) * 100;
  const maxPercent = (max / MAX) * 100;

  // Visual fill
  minSlider.style.background = `linear-gradient(to right, var(--green) ${minPercent}%, #cfcac4 ${minPercent}%)`;

  maxSlider.style.background = `linear-gradient(to right, var(--green) ${maxPercent}%, #cfcac4 ${maxPercent}%)`;
}

minSlider.addEventListener("input", updateSliders);
maxSlider.addEventListener("input", updateSliders);

updateSliders();