import React, { useEffect, useRef } from 'react';

const ParticlesBackground: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    // Create particles
    const particleCount = 50;
    const particles: HTMLDivElement[] = [];

    const createParticle = () => {
      const particle = document.createElement('div');
      particle.className = 'particle';
      particle.style.left = `${Math.random() * 100}%`;
      particle.style.setProperty('--offset-x', `${Math.random() * 200 - 100}px`);
      particles.push(particle);
      container.appendChild(particle);

      // Remove particle after animation
      particle.addEventListener('animationend', () => {
        particle.remove();
        particles.splice(particles.indexOf(particle), 1);
      });
    };

    // Initial particles
    for (let i = 0; i < particleCount; i++) {
      setTimeout(() => createParticle(), i * 200);
    }

    // Continuously create new particles
    const interval = setInterval(() => {
      if (particles.length < particleCount) {
        createParticle();
      }
    }, 1000);

    // Cleanup
    return () => {
      clearInterval(interval);
      particles.forEach(particle => particle.remove());
    };
  }, []);

  return <div ref={containerRef} className="particles-container" />;
};

export default ParticlesBackground;