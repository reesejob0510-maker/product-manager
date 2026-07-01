# HTML Engineering Guide

Full boilerplate and patterns for text-to-animated-html output.

## Minimal full-page boilerplate

```html
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=no">
  <title><!-- title --></title>
  <style>
    *,*::before,*::after { box-sizing: border-box; margin: 0; padding: 0; }
    /* paste platform CSS tokens here */

    .deck { position: fixed; inset: 0; overflow: hidden;
            display: flex; align-items: center; justify-content: center;
            background: var(--stage, var(--bg)); }

    .slide {
      position: absolute;
      /* platform dimensions here */
      opacity: 0; transform: translateY(28px);
      transition: transform 1.1s cubic-bezier(.4,0,.2,1), opacity 1.1s ease;
    }

    /* Generic entrance classes */
    .ai  { opacity: 0; transform: translateY(14px); }
    .al  { opacity: 0; transform: translateX(-14px); }
    .slide.go .ai { animation: fadeUp .5s ease forwards; }
    .slide.go .al { animation: fadeL  .5s ease forwards; }
    .slide.go .ai.d1 { animation-delay: .06s; }
    .slide.go .ai.d2 { animation-delay: .16s; }
    .slide.go .ai.d3 { animation-delay: .28s; }
    .slide.go .ai.d4 { animation-delay: .42s; }
    .slide.go .ai.d5 { animation-delay: .58s; }
    .slide.go .ai.d6 { animation-delay: .76s; }

    @keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeL  { to { opacity: 1; transform: translateX(0); } }
    @keyframes blink  { 0%,100%{opacity:1} 50%{opacity:0} }

    /* Nav */
    #dots { position: fixed; right: 14px; top: 50%; transform: translateY(-50%);
            display: flex; flex-direction: column; gap: 6px; z-index: 100; }
    .dot  { width: 5px; height: 5px; border-radius: 50%; background: var(--muted);
            cursor: pointer; transition: all .3s; }
    .dot.on { background: var(--accent); transform: scale(1.7); }
    #arrows { position: fixed; bottom: 16px; left: 50%; transform: translateX(-50%);
              display: flex; gap: 8px; z-index: 100; }
    .abtn { width: 30px; height: 30px; border-radius: 50%;
            border: 1px solid var(--border); background: var(--bg);
            color: var(--dim); font-size: 12px; cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            transition: all .2s; font-family: inherit; }
    .abtn:hover { border-color: var(--accent); color: var(--accent); }
    .abtn:disabled { opacity: .22; cursor: not-allowed; }
  </style>
</head>
<body>
<div class="deck">
  <div class="slide go" id="s0"><!-- SLIDE 0 --></div>
  <div class="slide"    id="s1"><!-- SLIDE 1 --></div>
</div>

<nav id="dots"></nav>
<div id="arrows">
  <button class="abtn" id="bp" onclick="goTo(cur-1)" disabled>↑</button>
  <button class="abtn" id="bn" onclick="goTo(cur+1)">↓</button>
</div>

<script>
const slides = [...document.querySelectorAll('.slide')];
const N = slides.length;
let cur = 0, lock = false;

// Build dot nav
const dotsEl = document.getElementById('dots');
slides.forEach((_, i) => {
  const d = document.createElement('div');
  d.className = 'dot' + (i === 0 ? ' on' : '');
  d.onclick = () => goTo(i);
  dotsEl.appendChild(d);
});

function ui() {
  [...document.querySelectorAll('.dot')].forEach((d, i) => d.classList.toggle('on', i === cur));
  document.getElementById('bp').disabled = cur === 0;
  document.getElementById('bn').disabled = cur === N - 1;
}

function pos(el, p) {
  if (p === 'c') { el.style.opacity = '1';  el.style.transform = 'translateY(0)'; }
  else if (p === 'a') { el.style.opacity = '0'; el.style.transform = 'translateY(-28px)'; }
  else               { el.style.opacity = '0'; el.style.transform = 'translateY(28px)'; }
}

function goTo(n) {
  if (n < 0 || n >= N || n === cur || lock) return;
  lock = true;
  const prev = cur, dir = n > prev ? 'dn' : 'up';
  cur = n;
  slides[cur].style.transition = 'none';
  pos(slides[cur], dir === 'dn' ? 'b' : 'a');
  slides[cur].classList.remove('go');
  void slides[cur].offsetWidth;          // force reflow — do not remove
  slides[cur].style.transition = '';
  pos(slides[cur], 'c');
  pos(slides[prev], dir === 'dn' ? 'a' : 'b');
  slides[prev].classList.remove('go');
  setTimeout(() => { slides[cur].classList.add('go'); trigger(cur); }, 120);
  setTimeout(() => { lock = false; }, 1300);  // must exceed transition duration
  ui();
}

function trigger(n) {
  const s = slides[n];
  // Reset and replay all countUp elements on this slide
  s.querySelectorAll('[data-cu]').forEach(el => {
    el.textContent = '0' + (el.dataset.suffix || '');
    cntUp(el, 3000);
  });
  // Add per-slide triggers below (countUp2, progressBar, typewriter, highlightPulse)
}

function cntUp(el, dur) {
  const t = parseFloat(el.dataset.target), sf = el.dataset.suffix || '';
  const inc = t / (dur / 16); let v = 0;
  const tid = setInterval(() => {
    v = Math.min(v + inc, t);
    el.textContent = Math.floor(v) + sf;
    if (v >= t) { el.textContent = t + sf; clearInterval(tid); }
  }, 16);
}
function cntUp2(el, t, dur) {
  const inc = t / (dur / 16); let v = 0;
  const tid = setInterval(() => {
    v = Math.min(v + inc, t); el.textContent = Math.floor(v);
    if (v >= t) { el.textContent = t; clearInterval(tid); }
  }, 16);
}
function cntUpDec(el, t, dur) {
  const inc = t / (dur / 16); let v = 0;
  const tid = setInterval(() => {
    v = Math.min(v + inc, t); el.textContent = v.toFixed(1);
    if (v >= t) { el.textContent = t.toFixed(1); clearInterval(tid); }
  }, 16);
}

// ── CRITICAL: Initialize first slide ──
slides[0].style.opacity = '1';
slides[0].style.transform = 'translateY(0)';
trigger(0); ui();

// Keyboard navigation
document.addEventListener('keydown', e => {
  if ([' ', 'ArrowDown', 'ArrowRight'].includes(e.key)) { e.preventDefault(); goTo(cur + 1); }
  if (['ArrowUp', 'ArrowLeft'].includes(e.key)) { e.preventDefault(); goTo(cur - 1); }
});

// Touch / swipe
let ty0 = 0;
document.addEventListener('touchstart', e => { ty0 = e.touches[0].clientY; }, { passive: true });
document.addEventListener('touchend', e => {
  const dy = e.changedTouches[0].clientY - ty0;
  if (Math.abs(dy) > 50) goTo(dy < 0 ? cur + 1 : cur - 1);
}, { passive: true });

// Mouse wheel
let wt;
document.addEventListener('wheel', e => {
  e.preventDefault();
  clearTimeout(wt);
  wt = setTimeout(() => {
    if (e.deltaY > 15) goTo(cur + 1);
    else if (e.deltaY < -15) goTo(cur - 1);
  }, 90);
}, { passive: false });
</script>
</body>
</html>
```

## Common bugs and fixes

### Bug: First slide is invisible
**Cause**: `.slide` starts at `opacity:0; transform:translateY(28px)` by CSS. The first slide never goes through `goTo()`, so it stays hidden.
**Fix**: Always add after slides array is built:
```javascript
slides[0].style.opacity = '1';
slides[0].style.transform = 'translateY(0)';
```

### Bug: Animations don't replay when returning to a slide
**Cause**: CSS animations with `forwards` fill mode don't replay on class re-add unless a reflow is forced.
**Fix**: In `goTo()`, always do:
```javascript
slides[cur].classList.remove('go');
void slides[cur].offsetWidth;   // this line is essential
slides[cur].classList.add('go');
```

### Bug: countUp shows wrong value on revisit
**Cause**: `trigger(n)` didn't reset `el.textContent` before starting the interval.
**Fix**: In `trigger(n)`:
```javascript
el.textContent = '0' + (el.dataset.suffix || '');
cntUp(el, 3000);
```

### Bug: Page transition shows previous slide on top
**Cause**: Absolutely positioned slides stack in DOM order. Without z-index, earlier slides may obscure later ones during transition.
**Fix**: Give the incoming slide a higher z-index during transition:
```javascript
slides[cur].style.zIndex = '2';
slides[prev].style.zIndex = '1';
setTimeout(() => { slides[prev].style.zIndex = ''; slides[cur].style.zIndex = ''; }, 1300);
```

### Bug: Lock timeout too short causes broken transitions
**Cause**: `lock = false` fires before the transition finishes, allowing a second `goTo()` call mid-animation.
**Fix**: Lock timeout must always exceed the transition duration + 150 ms buffer. For 1.1s transition: `setTimeout(() => lock = false, 1300)`.
