const destinationUrls = ['destination1.html','destination2.html','destination3.html','destination4.html','destination5.html','destination6.html'];

function surpriseMe() {
  const current = window.location.pathname.toLowerCase();
  const available = destinationUrls.filter(url => !current.includes(url.replace('.html', '')));
  const next = available.length
    ? available[Math.floor(Math.random() * available.length)]
    : destinationUrls[Math.floor(Math.random() * destinationUrls.length)];
  window.location.href = next;
}
