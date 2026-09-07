'use strict';
const mobile = document.querySelector('.mobile-nav details');
if (mobile) mobile.addEventListener('click', event => {
  if (event.target.closest('a[href^="#"]')) mobile.open = false;
});
const headings = [...document.querySelectorAll('article h2')];
const links = [...document.querySelectorAll('.toc a')];
let scheduled = false;
function updateLocation() {
  scheduled = false;
  let current = headings[0];
  for (const heading of headings) {
    if (heading.getBoundingClientRect().top <= 140) current = heading;
    else break;
  }
  links.forEach(link => {
    if (current && link.hash === '#' + current.id) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
}
window.addEventListener('scroll', () => {
  if (!scheduled) { scheduled = true; requestAnimationFrame(updateLocation); }
}, { passive: true });
updateLocation();
