'use strict';
(() => {
 const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let motionPaused=false;
 const running=new Set();
 const canMove=()=>!reduced.matches&&!motionPaused;
 function animate(el,frames,options={}){
  if(!canMove()||!el?.animate)return null;
  const animation=el.animate(frames,{duration:620,easing:'cubic-bezier(.18,.72,.2,1)',...options});
  running.add(animation);animation.finished.catch(()=>{}).finally(()=>running.delete(animation));return animation;
 }
 function syncMotion(){
  const paused=!canMove();document.body.classList.toggle('motion-paused',paused);
  $$('.motion-toggle').forEach(button=>{button.textContent=reduced.matches?'Reduced motion':motionPaused?'Resume motion':'Pause motion';button.disabled=reduced.matches;button.setAttribute('aria-pressed',String(paused));});
  if(paused){running.forEach(animation=>{try{animation.finish();}catch{animation.cancel();}});$$('.reveal-pending').forEach(el=>el.classList.remove('reveal-pending'));if(stage){stage.style.setProperty('--stage-x','0px');stage.style.setProperty('--stage-y','0px');}}
 }
 $$('.motion-toggle').forEach(button=>button.addEventListener('click',()=>{motionPaused=!motionPaused;syncMotion();}));
 const menu=$('#mobile-menu'), toggle=$('.menu-toggle');
 function setMenu(open){menu.hidden=!open;toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');if(!open)$$('details',menu).forEach(d=>d.open=false);}
 toggle.addEventListener('click',()=>setMenu(menu.hidden));
 $$('a',menu).forEach(a=>a.addEventListener('click',()=>setMenu(false)));
 $$('.nav-disclosure').forEach(d=>{
  $$('.nav-dropdown a',d).forEach((link,i)=>link.style.setProperty('--link-order',i));
  $('summary',d).addEventListener('click',()=>{if(!d.open)$$('.nav-disclosure').forEach(other=>{if(other!==d)other.open=false;});});
 });
 document.addEventListener('click',event=>{$$('.nav-disclosure[open]').forEach(d=>{if(!d.contains(event.target))d.open=false;});if(!menu.hidden&&!$('.site-header').contains(event.target))setMenu(false);});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'){const opened=$$('.nav-disclosure[open]');opened.forEach(d=>d.open=false);if(!menu.hidden){setMenu(false);toggle.focus();}else if(opened.length)$('summary',opened[0]).focus();}});
 $('.site-header').addEventListener('focusout',()=>setTimeout(()=>{$$('.desktop-nav .nav-disclosure[open]').forEach(d=>{if(!d.contains(document.activeElement))d.open=false;});},0));
 matchMedia('(min-width: 1051px)').addEventListener('change',e=>{if(e.matches)setMenu(false);});
 $$('a').forEach(a=>{const u=new URL(a.href,location.href);if(u.origin===location.origin&&u.pathname===location.pathname&&!u.hash)a.setAttribute('aria-current','page');});
 const stage=$('[data-hero-stage]');let frame=0;
 if(stage){stage.addEventListener('pointermove',event=>{if(!canMove()||!matchMedia('(pointer:fine)').matches)return;const r=stage.getBoundingClientRect();if(frame)cancelAnimationFrame(frame);frame=requestAnimationFrame(()=>{stage.style.setProperty('--stage-x',((event.clientX-r.left)/r.width*14-7)+'px');stage.style.setProperty('--stage-y',((event.clientY-r.top)/r.height*12-6)+'px');frame=0;});},{passive:true});stage.addEventListener('pointerleave',()=>{if(frame)cancelAnimationFrame(frame);stage.style.setProperty('--stage-x','0px');stage.style.setProperty('--stage-y','0px');});}
 const steps=[
  ['A clear starting point','New enquiry','Every enquiry, in one place.','Capture the details that help your team understand what a customer needs.','Next: find the right person'],
  ['A clear responsibility','Assigned','The right person. The right context.','Give the responsible team member the information they need to take the next step.','Next: keep the work moving'],
  ['A clear overview','In progress','See what needs to happen next.','Follow the work through a shared view of ownership, status and next actions.','One connected, illustrative workflow']
 ];
 $$('[data-step]').forEach(button=>button.addEventListener('click',()=>{const i=Number(button.dataset.step);['label','status','title','copy','next'].forEach((key,n)=>$('#workflow-'+key).textContent=steps[i][n]);$$('[data-step]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));$$('.workflow-bars i').forEach((bar,n)=>bar.classList.toggle('on',n<=i));animate($('.workflow-body'),[{opacity:.3,transform:'translateY(7px)'},{opacity:1,transform:'translateY(0)'}]);}));
 $$('[data-filter]').forEach(button=>button.addEventListener('click',()=>{let count=0;$$('.project-directory article').forEach(card=>{card.hidden=button.dataset.filter!=='all'&&card.dataset.category!==button.dataset.filter;if(!card.hidden)count++;});$$('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));$('.filter-status').textContent='Showing '+count+' selected projects';}));
 const form=$('#enquiry-form'),mode=$('#enquiry-mode');
 if(form){
  const serviceChecks=$$('input[name=services]',form);
  function serviceValidity(){serviceChecks[0].setCustomValidity(mode.value==='studio'&&!serviceChecks.some(c=>c.checked)?'Select at least one service.':'');}
  function changeMode(value){mode.value=['studio','network','experience','general'].includes(value)?value:'studio';const network=mode.value==='network',studio=mode.value==='studio',updates=mode.value==='experience';$$('[data-network-only]').forEach(field=>{field.hidden=!network;const input=$('input',field);input.disabled=!network;input.required=network;});$('#service-interests').hidden=!studio;serviceChecks.forEach(c=>c.disabled=!studio);$('#organisation').required=studio||network;$('#message').required=!updates;$('#message-label').textContent=network?'Tell us about your role and what you’re navigating':updates?'Anything you would like to add? (optional)':'What are you hoping to achieve?';serviceValidity();}
  mode.addEventListener('change',()=>changeMode(mode.value));serviceChecks.forEach(c=>c.addEventListener('change',serviceValidity));
  const hashMode=()=>{const value=location.hash.slice(1);if(!value||['studio','network','experience','general'].includes(value))changeMode(value);};addEventListener('hashchange',hashMode);hashMode();
  form.addEventListener('submit',event=>{event.preventDefault();serviceValidity();if(!form.reportValidity())return;form.hidden=true;$('#form-success').hidden=false;$('#form-success').focus();});
  $('#reset-form').addEventListener('click',()=>{form.hidden=false;$('#form-success').hidden=true;mode.focus();});
 }

 if('IntersectionObserver'in window){
  const targets=$$('.section-heading,.project-card,.audience-grid>a,.workflow,.network-teaser>div,.editorial-row,.service-row,.team-grid>article,.resource-grid>article,.experience-feature>div,.contact-layout>aside,.contact-form-wrap,.collaboration-frame,.collaboration-caption,.footer-cta>div,.footer-arrow');
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
   if(!entry.isIntersecting)return;
   const el=entry.target;el.classList.remove('reveal-pending');
   const row=el.matches('.editorial-row,.service-row');
   animate(el,[{opacity:0,transform:row?'translateX(32px)':'translateY(52px) scale(.98)'},{opacity:1,transform:'translate(0,0) scale(1)'}],{duration:900,delay:Number(el.dataset.revealDelay||0),fill:'backwards'});
   observer.unobserve(el);
  }),{threshold:.09,rootMargin:'0px 0px 35px 0px'});
  targets.forEach(el=>{
   if(el.getBoundingClientRect().top>innerHeight+30){
    el.dataset.revealDelay=String(Math.min([...el.parentElement.children].indexOf(el)*80,240));
    if(canMove())el.classList.add('reveal-pending');observer.observe(el);
   }
  });
  document.addEventListener('focusin',event=>{const el=event.target.closest('.reveal-pending');if(el){el.classList.remove('reveal-pending');observer.unobserve(el);}});
 }
 reduced.addEventListener('change',syncMotion);
 syncMotion();
})();
