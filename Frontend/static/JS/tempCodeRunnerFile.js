if (min > max) {
    minSlider.value = max;
    min = max;
  }

  if (max < min) {
    maxSlider.value = min;
    max = min;
  }