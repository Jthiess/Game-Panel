// Simple horizontal scroll buttons for each carousel
document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.carousel-btn');
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target') === 'middle' ? 'carousel-middle' : 'carousel-bottom';
      const dir = btn.getAttribute('data-dir');
      const container = document.getElementById(targetId);
      if (!container) return;
      const amount = Math.round(container.clientWidth * 0.8);
      container.scrollBy({ left: dir === 'left' ? -amount : amount, behavior: 'smooth' });
    });
  });

  // Enable mouse drag to scroll horizontally and handle wheel events
  const draggables = document.querySelectorAll('.carousel-row');
  draggables.forEach(drag => {
    let isDown = false;
    let startX, scrollLeft;

    // Prevent text selection while dragging
    drag.style.userSelect = 'none';
    drag.style.webkitUserSelect = 'none';
    drag.style.msUserSelect = 'none';

    // Prevent images inside the carousel from starting native drag operations
    // This avoids the browser drag ghost when the user is trying to drag-scroll the carousel.
    const imgs = drag.querySelectorAll('img');
    imgs.forEach(img => {
      try { img.draggable = false; } catch (err) { /* ignore */ }
      img.addEventListener('dragstart', (ev) => ev.preventDefault());
    });
    drag.addEventListener('mousedown', (e) => {
      isDown = true;
      drag.classList.add('dragging');
      startX = e.pageX - drag.offsetLeft;
      scrollLeft = drag.scrollLeft;
    });

    window.addEventListener('mouseup', () => {
      isDown = false;
      drag.classList.remove('dragging');
    });

    drag.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - drag.offsetLeft;
      const walk = (x - startX) * 1; // scroll-fast multiplier
      drag.scrollLeft = scrollLeft - walk;
    });

    // Handle wheel events for horizontal scrolling
    drag.addEventListener('wheel', (e) => {
      e.preventDefault(); // Prevent vertical scrolling
      drag.scrollBy({
        left: e.deltaY,
        behavior: 'smooth'
      });
    });
  });
});
