'use strict';

const demoAssetRoot = new URL('.', document.currentScript.src);
const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
const menuButton = $('.menu-toggle');
const mobileMenu = $('#mobile-menu');

function setMenu(open) {
  if (open) setDesktopMenu(null);
  mobileMenu.hidden = !open;
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
}
menuButton.addEventListener('click', () => setMenu(mobileMenu.hidden));
$$('a, [data-contact]', mobileMenu).forEach(link => link.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !mobileMenu.hidden) { setMenu(false); menuButton.focus(); }
});
document.addEventListener('click', event => {
  if (!mobileMenu.hidden && !mobileMenu.contains(event.target) && !menuButton.contains(event.target)) setMenu(false);
});
matchMedia('(min-width: 1051px)').addEventListener('change', event => { if (event.matches) setMenu(false); });
const header = $('.site-header');
addEventListener('scroll', () => header.classList.toggle('scrolled', scrollY > 20), { passive: true });

// Anchor navigation reflects the section currently being read.
const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      $$('.desktop-nav [data-nav-section]').forEach(link => {
        const active = link.dataset.navSection === entry.target.id;
        link.classList.toggle('active', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
  });
}, { rootMargin: '-20% 0px -55% 0px', threshold: 0 });
$$('main > section[id]').forEach(section => sectionObserver.observe(section));

// Keep the services readable as one deliberate, expandable list.
const servicePanels = $$('.service');
servicePanels.forEach(panel => $('summary', panel).addEventListener('click', () => {
  // Close peers before the native click opens this item; initial toggle events
  // must not race a section selected by a cross-page fragment.
  if (!panel.open) servicePanels.forEach(other => { if (other !== panel) other.open = false; });
}));

const grid = $('#projects-grid');
const moreButton = $('#more-projects');
let currentFilter = 'all';
let expanded = false;
function filterProjects() {
  if (!grid) return;
  grid.classList.toggle('filtered', currentFilter !== 'all');
  grid.classList.toggle('expanded', expanded);
  $$('.project-card', grid).forEach(card => { card.hidden = currentFilter !== 'all' && card.dataset.category !== currentFilter; });
  $$('[data-filter]').forEach(button => {
    const active = button.dataset.filter === currentFilter;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  });
  moreButton.hidden = currentFilter !== 'all';
  moreButton.setAttribute('aria-expanded', String(expanded));
  moreButton.innerHTML = (expanded ? 'Show selected highlights' : 'More of the work') + ' <span aria-hidden="true">' + (expanded ? '−' : '↗') + '</span>';
  const count = $$('.project-card', grid).filter(card => !card.hidden && getComputedStyle(card).display !== 'none').length;
  $('.filter-status').textContent = count + ' selected projects shown';
}
$$('[data-filter]').forEach(button => button.addEventListener('click', () => { currentFilter = button.dataset.filter; filterProjects(); }));
moreButton?.addEventListener('click', () => { expanded = !expanded; filterProjects(); });

const contactDialog = $('#contact-dialog');
const detailDialog = $('#detail-dialog');
const form = $('#enquiry-form');
const formSuccess = $('#form-success');
let activeContact = 'studio';
const contactCopy = {
  studio: { title: 'Bring your vision to life.', description: 'A free 30-minute strategy call is the first step.', organisation: true, interest: true, message: true },
  network: { title: 'Find your people.', description: 'Membership begins with consideration and a private 20-minute call.', organisation: true, interest: false, message: true },
  updates: { title: 'Stay in the conversation.', description: 'Hear about planned gatherings and The Shepherd’s Diary.', organisation: false, interest: false, message: false },
  general: { title: 'Start a conversation.', description: 'A question, a collaboration, or something else on your mind.', organisation: false, interest: false, message: true }
};
function setContact(type) {
  activeContact = contactCopy[type] ? type : 'studio';
  const copy = contactCopy[activeContact];
  $('#contact-title').textContent = copy.title;
  $('#contact-description').textContent = copy.description;
  ['organisation', 'interest', 'message'].forEach(name => {
    const field = $('#' + name + '-field');
    field.hidden = !copy[name];
    const input = $('input, textarea, select', field);
    input.disabled = !copy[name];
    if (name !== 'interest') input.required = Boolean(copy[name]);
  });
  $$('[data-contact-tab]').forEach(tab => {
    const selected = tab.dataset.contactTab === activeContact;
    tab.setAttribute('aria-selected', String(selected));
    tab.tabIndex = selected ? 0 : -1;
    tab.id = 'enquiry-tab-' + tab.dataset.contactTab;
  });
  form.setAttribute('aria-labelledby', 'enquiry-tab-' + activeContact);
  form.hidden = false;
  formSuccess.hidden = true;
}
function openContact(type = 'studio', service) {
  setDesktopMenu(null);
  setMenu(false);
  form.reset();
  setContact(type);
  if (service) form.elements.interest.value = service;
  if (detailDialog.open) detailDialog.close();
  if (!contactDialog.open) contactDialog.showModal();
  document.body.classList.add('dialog-open');
}
$$('[data-contact]').forEach(button => button.addEventListener('click', () => openContact(button.dataset.contact)));
$$('[data-service]').forEach(button => button.addEventListener('click', () => openContact('studio', button.dataset.service)));
$$('[data-contact-tab]').forEach(tab => tab.addEventListener('click', () => setContact(tab.dataset.contactTab)));
$('.contact-tabs').addEventListener('keydown', event => {
  if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
  event.preventDefault();
  const tabs = $$('[data-contact-tab]');
  const index = tabs.indexOf(document.activeElement);
  const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
  setContact(tabs[next].dataset.contactTab);
  tabs[next].focus();
});
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  // Presentation-only: no requests, storage, mailing lists, or production writes.
  form.hidden = true;
  formSuccess.hidden = false;
  formSuccess.tabIndex = -1;
  formSuccess.focus();
});

const projects = {
  springs: { title: 'Springs Gate Chapel', category: 'Church & community', image: 'assets/springs-gate.webp', description: 'A church website bringing service information, ministries, livestream access, and visitor next steps into one welcoming digital home.', facts: ['Church website', 'Lake Ridge, Virginia'], url: 'https://springsgatechapel.org/' },
  rengov: { title: 'Rengovtech Dubai', category: 'Technology & security', image: 'assets/rengovtech.webp', description: 'A corporate digital presence for an IT, software, and cyber-security consultancy, bringing a broad technical offer into clear focus.', facts: ['Corporate website', 'IT & cyber-security'], url: 'https://rengovtechdubai.com/' },
  cire: { title: 'Cire Homes', category: 'Property & hospitality', image: 'assets/cire-homes.webp', description: 'A website for an Atlanta short-term rental management business, presenting property management, cleaning, maintenance, and pricing.', facts: ['Property website', 'Atlanta, Georgia'], url: 'https://cirehomes.com/' },
  base: { title: 'The Base Marketing', category: 'Digital & marketing', image: 'assets/base-marketing.webp', description: 'A bold agency website connecting web design, search, social media, and paid advertising in a clear service-led experience.', facts: ['Agency website', 'Digital marketing'], url: 'https://thebasemarketing.com/' },
  recharge: { title: 'Recharge Global', category: 'Youth & ministry', image: 'assets/recharge.webp', description: 'An expressive website for a Christ-centred youth and campus movement, bringing events, stories, film, and giving opportunities together.', facts: ['Ministry website', 'Youth & campus movement'], url: 'https://rechargeglobal.org/' },
  faircross: { title: 'Faircross', category: 'Construction & property', image: 'assets/faircross.webp', description: 'A modern web presence introducing construction and real estate expertise through a considered, service-focused presentation.', facts: ['Business website', 'Construction & property'], url: 'https://faircross.co.uk/' }
};
const experiences = {
  roundtable: { title: 'The Shepherd’s Roundtable', category: 'An invitation to a different kind of room', image: 'assets/conversation.jpg', description: 'An invitation-only gathering for senior pastors and ministry leaders. Equal voices, a confidential conversation, and no stage. Each session moves from a shared question to open discussion, individual commitments, and connection between gatherings.', facts: ['June 2027 · planned', 'Quarterly', '8–12 leaders'] },
  dinner: { title: 'Leadership Dinners', category: 'A shared table. A little more perspective.', image: 'assets/dinner.jpg', description: 'Private evenings for a carefully considered group of 8–12 leaders. An opportunity to share a meal, exchange perspectives, and form relationships away from the expectations of a public platform. The first planned dinner is in Atlanta; a date has not been announced.', facts: ['Atlanta, Georgia · planned', '8–12 leaders', 'By invitation'] },
  retreat: { title: 'Leadership Retreats', category: 'Space to think. Space to reconnect.', image: 'assets/retreat.webp', description: 'Time away from the everyday demands of leadership, with conversation-led sessions and room for rest. The inaugural retreat is planned for the third quarter of 2027. Location and final details will be shared with invited leaders.', facts: ['Q3 2027 · planned', 'Private gathering', 'Location to be confirmed'] }
};
function showDetail(data, experience = false) {
  setDesktopMenu(null);
  const image = $('#detail-image');
  image.src = new URL(data.image, demoAssetRoot).href;
  image.alt = data.title + (experience ? ' gathering imagery' : ' website preview');
  $('#detail-title').textContent = data.title;
  $('#detail-category').textContent = data.category;
  $('#detail-description').textContent = data.description;
  $('#detail-facts').replaceChildren(...data.facts.map(fact => {
    const span = document.createElement('span'); span.className = 'detail-fact'; span.textContent = fact; return span;
  }));
  $('#detail-link').hidden = experience;
  $('#detail-enquire').hidden = !experience;
  if (!experience) $('#detail-link').href = data.url;
  $('#detail-attribution').textContent = experience ? 'Planned experiences from Ascend Brand Network. Participation is subject to review and invitation.' : 'Project delivered by members of the Ascend Studio founding team. Original portfolio imagery.';
  detailDialog.classList.toggle('experience-detail', experience);
  if (!detailDialog.open) detailDialog.showModal();
  document.body.classList.add('dialog-open');
}
$$('[data-project]').forEach(button => button.addEventListener('click', () => showDetail(projects[button.dataset.project])));
$$('[data-experience]').forEach(button => button.addEventListener('click', () => showDetail(experiences[button.dataset.experience], true)));
$('#detail-enquire').addEventListener('click', () => openContact('updates'));
$$('dialog').forEach(dialog => {
  dialog.setAttribute('aria-labelledby', dialog === contactDialog ? 'contact-title' : 'detail-title');
  $('[data-close]', dialog).addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => {
    if (!$$('dialog').some(item => item.open)) document.body.classList.remove('dialog-open');
  });
});
filterProjects();


// Two editorial navigation panels keep the pitch rich without adding pages.
const navTriggers = $$('[data-nav-menu]');
const navPanels = $$('.nav-panel');
const navScrim = $('.navigation-scrim');
let openDesktopMenu = null;
let desktopOpenedByHover = false;
function setDesktopMenu(key, restoreFocus = false) {
  const previous = openDesktopMenu;
  desktopOpenedByHover = false;
  openDesktopMenu = key;
  navTriggers.forEach(trigger => trigger.setAttribute('aria-expanded', String(trigger.dataset.navMenu === key)));
  navPanels.forEach(panel => { panel.hidden = panel.id !== key + '-nav-panel'; });
  navScrim.hidden = key === null;
  header.classList.toggle('menu-is-open', key !== null);
  if (restoreFocus && previous) $('[data-nav-menu="' + previous + '"]').focus();
}
navTriggers.forEach(trigger => trigger.addEventListener('click', () => {
  if (openDesktopMenu === trigger.dataset.navMenu && desktopOpenedByHover) { desktopOpenedByHover = false; return; }
  setDesktopMenu(openDesktopMenu === trigger.dataset.navMenu ? null : trigger.dataset.navMenu);
}));
navScrim.addEventListener('click', () => setDesktopMenu(null));
navPanels.forEach(panel => {
  $$('a', panel).forEach(link => link.addEventListener('click', () => setDesktopMenu(null)));
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && openDesktopMenu) setDesktopMenu(null, true);
});
header.addEventListener('focusout', () => {
  setTimeout(() => { if (!header.contains(document.activeElement)) setDesktopMenu(null); }, 0);
});
$$('[data-nav-service]').forEach(button => button.addEventListener('click', () => {
  setDesktopMenu(null);
  const selected = servicePanels[Number(button.dataset.navService)];
  servicePanels.forEach(panel => { panel.open = panel === selected; });
  selected.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start' });
  const summary = $('summary', selected);
  summary.focus({ preventScroll: true });
}));
matchMedia('(max-width: 1050px)').addEventListener('change', event => { if (event.matches) setDesktopMenu(null); });
const progressBar = $('.reading-progress span');
const backToTop = $('.back-to-top');
let progressQueued = false;
function updateReadingProgress() {
  const maximum = document.documentElement.scrollHeight - innerHeight;
  progressBar.style.transform = 'scaleX(' + (maximum > 0 ? Math.min(1, scrollY / maximum) : 0) + ')';
  backToTop.hidden = scrollY < 1100;
  progressQueued = false;
}
addEventListener('scroll', () => {
  if (!progressQueued) { progressQueued = true; requestAnimationFrame(updateReadingProgress); }
}, { passive: true });
addEventListener('resize', updateReadingProgress);
backToTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' });
  $('.brand').focus({ preventScroll: true });
});
updateReadingProgress();



// Preserve the original menu behaviour across all static destinations.
let menuCloseTimer;
navTriggers.forEach(trigger => trigger.addEventListener('mouseenter', () => {
  if (matchMedia('(min-width: 1051px) and (hover: hover)').matches) {
    clearTimeout(menuCloseTimer);
    if (openDesktopMenu !== trigger.dataset.navMenu) { setDesktopMenu(trigger.dataset.navMenu); desktopOpenedByHover = true; }
  }
}));
header.addEventListener('mouseenter', () => clearTimeout(menuCloseTimer));
header.addEventListener('mouseleave', () => {
  if (matchMedia('(hover: hover)').matches) menuCloseTimer = setTimeout(() => setDesktopMenu(null), 220);
});
$$('.desktop-nav > a').forEach(link => link.addEventListener('mouseenter', () => setDesktopMenu(null)));
$$('.mobile-nav-group').forEach(group => group.addEventListener('toggle', () => {
  if (group.open) $$('.mobile-nav-group').forEach(other => { if (other !== group) other.open = false; });
}));
function resolvePageFragment() {
  const hash = decodeURIComponent(location.hash.slice(1));
  if (document.body.dataset.page === 'work-with-us') {
    const modes = { network: 'network', studio: 'studio', experience: 'updates', general: 'general' };
    if (modes[hash]) openContact(modes[hash]);
  } else {
    const target = document.getElementById(hash);
    if (target?.matches('details.service')) {
      servicePanels.forEach(panel => { panel.open = panel === target; });
      requestAnimationFrame(() => target.scrollIntoView({ block: 'start', behavior: 'instant' }));
    }
  }
}
addEventListener('hashchange', resolvePageFragment);
resolvePageFragment();
