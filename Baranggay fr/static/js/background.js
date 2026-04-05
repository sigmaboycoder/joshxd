
document.addEventListener("DOMContentLoaded", function () {
  const particlesContainer = document.getElementById("particles");
  if (!particlesContainer) return;

  const numParticles = 120;
  for (let i = 0; i < numParticles; i++) {
    const p = document.createElement("div");
    p.classList.add("particle");
    const size = Math.random() * 3 + 1;
    p.style.width = `${size}px`;
    p.style.height = `${size}px`;
    p.style.left = `${Math.random() * 100}%`;
    p.style.top = `${Math.random() * 100}%`;
    p.style.animationDuration = `${10 + Math.random() * 10}s`;
    p.style.animationDelay = `${Math.random() * 10}s`;
    particlesContainer.appendChild(p);
  }
});

