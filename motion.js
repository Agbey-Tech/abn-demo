/* Progressive motion: no dependency, no loading gate, and no scroll hijacking. */
(() => {
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)');
  const running = new Set();
  let revealObserver;
  let enabled = !preference.matches;
  const motionElements = new Set();

  function play(element, frames, options) {
    if (!enabled || !element.animate) return null;
    const animation = element.animate(frames, options);
    running.add(animation);
    animation.finished.catch(() => {}).finally(() => running.delete(animation));
    return animation;
  }

  function setupReveals() {
    if (!enabled || !('IntersectionObserver' in window)) return;
    const selectors = '.section-top,.split-heading,.division,.network-copy,.network-photo,.network-bottom,.service,.studio-proof,.work-heading,.project-card,.work-foot,.experience-card,.journal-image,.journal-copy,.closing-main,.closing-paths,.interior-section>div';
    const targets = [...document.querySelectorAll(selectors)];
    revealObserver = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting);
      visible.forEach((entry, index) => {
        const element = entry.target;
        element.classList.remove('is-reveal-queued');
        play(element, [{ opacity: 0, transform: 'translateY(27px)' }, { opacity: 1, transform: 'translateY(0)' }], {
          duration: 780, delay: Math.min(index * 65, 195), easing: 'cubic-bezier(.18,.7,.2,1)', fill: 'backwards'
        });
        revealObserver.unobserve(element);
      });
    }, { threshold: 0.06, rootMargin: '0px 0px -15px 0px' });
    targets.forEach(element => {
      if (element.getBoundingClientRect().top > innerHeight + 20) {
        element.classList.add('is-reveal-queued');
        motionElements.add(element);
        revealObserver.observe(element);
      }
    });
  }

  const scene = document.querySelector('[data-hero-scene]');
  const hero = document.querySelector('.cinematic-hero');
  let sceneFrame = 0;
  let sceneX = 0, sceneY = 0;
  if (hero && scene) {
    hero.addEventListener('pointermove', event => {
      if (!enabled || !finePointer.matches || innerWidth < 1051) return;
      const bounds = hero.getBoundingClientRect();
      sceneX = ((event.clientX - bounds.left) / bounds.width - 0.5) * 12;
      sceneY = ((event.clientY - bounds.top) / bounds.height - 0.5) * 9;
      if (!sceneFrame) sceneFrame = requestAnimationFrame(() => {
        scene.style.setProperty('--scene-x', sceneX.toFixed(2) + 'px');
        scene.style.setProperty('--scene-y', sceneY.toFixed(2) + 'px');
        sceneFrame = 0;
      });
    }, { passive: true });
    hero.addEventListener('pointerleave', () => {
      if (sceneFrame) cancelAnimationFrame(sceneFrame);
      sceneFrame = 0;
      scene.style.setProperty('--scene-x', '0px');
      scene.style.setProperty('--scene-y', '0px');
    });
  }

  document.querySelectorAll('.hero-actions .button,.closing-arrow').forEach(button => {
    button.addEventListener('pointermove', event => {
      if (!enabled || !finePointer.matches) return;
      const rect = button.getBoundingClientRect();
      const x = (event.clientX - rect.left - rect.width / 2) * 0.06;
      const y = (event.clientY - rect.top - rect.height / 2) * 0.12;
      button.style.translate = x.toFixed(2) + 'px ' + y.toFixed(2) + 'px';
    }, { passive: true });
    button.addEventListener('pointerleave', () => { button.style.translate = '0px 0px'; });
  });

  document.querySelectorAll('[data-filter],#more-projects').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.project-card').forEach((card, index) => {
        if (!card.hidden && getComputedStyle(card).display !== 'none') {
          card.classList.remove('is-reveal-queued');
          revealObserver?.unobserve(card);
          play(card, [{ opacity: 0, transform: 'translateY(15px)' }, { opacity: 1, transform: 'translateY(0)' }], {
            duration: 500, delay: index * 45, easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards'
          });
        }
      });
    });
  });

  // Native dialogs retain focus management; movement only enhances their entry.
  const dialogObserver = new MutationObserver(records => {
    records.forEach(record => {
      const dialog = record.target;
      if (dialog.open) play(dialog, [{ opacity: 0, transform: 'translateY(18px) scale(.985)' }, { opacity: 1, transform: 'translateY(0) scale(1)' }], {
        duration: 380, easing: 'cubic-bezier(.18,.7,.2,1)'
      });
    });
  });
  document.querySelectorAll('dialog').forEach(dialog => dialogObserver.observe(dialog, { attributes: true, attributeFilter: ['open'] }));

  // Keep normal links, new-tab gestures and fragment navigation intact.
  let departure;
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href]');
    if (!enabled || !link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || link.target || link.hasAttribute('download')) return;
    const destination = new URL(link.href, location.href);
    if (destination.origin !== location.origin || destination.pathname === location.pathname || !['http:', 'https:'].includes(destination.protocol)) return;
    const main = document.querySelector('main');
    if (!main || departure) return;
    event.preventDefault();
    departure = play(main, [{ opacity: 1, transform: 'translateY(0)' }, { opacity: 0, transform: 'translateY(-8px)' }], { duration: 180, easing: 'ease-in', fill: 'forwards' });
    if (departure) departure.finished.then(() => location.assign(destination.href)).catch(() => {});
    else location.assign(destination.href);
  });
  addEventListener('pageshow', () => { departure?.cancel(); departure = null; });

  preference.addEventListener('change', () => {
    enabled = !preference.matches;
    if (!enabled) {
      revealObserver?.disconnect();
      running.forEach(animation => animation.cancel());
      motionElements.forEach(element => element.classList.remove('is-reveal-queued'));
      document.querySelectorAll('.hero-actions .button,.closing-arrow').forEach(button => { button.style.translate = 'none'; });
      if (scene) { scene.style.setProperty('--scene-x','0px'); scene.style.setProperty('--scene-y','0px'); }
    } else setupReveals();
  });

  setupReveals();
})();
