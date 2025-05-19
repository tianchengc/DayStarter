import { anime } from 'animejs';

export function animateMessage(): void {
  anime({
    targets: '.message',
    opacity: [0, 1],
    translateY: [-20, 0],
    duration: 1000,
    easing: 'easeOutExpo',
  });
}