# Animation Tokens

Full keyframe library for text-to-animated-html. All animations are CSS-only, no external libraries.

## Core entrance animations

### fadeUp
Standard entrance for most elements.
```css
@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }
.ai { opacity: 0; transform: translateY(14px); }
.slide.go .ai { animation: fadeUp 0.5s ease forwards; }
/* Stagger with .d1–.d6: delay 0.08s, 0.18s, 0.30s, 0.44s, 0.60s, 0.78s */
```

### fadeL
Entrance from the left. Used for list items, keyword map rows.
```css
@keyframes fadeL { to { opacity: 1; transform: translateX(0); } }
.al { opacity: 0; transform: translateX(-14px); }
.slide.go .al { animation: fadeL 0.5s ease forwards; }
```

### stampIn
Bold pop-in for icons, brand names, first-appearance reveals.
```css
@keyframes stampIn {
  0%   { transform: scale(0) rotate(-20deg); opacity: 0; }
  60%  { transform: scale(1.3) rotate(6deg);  opacity: 1; }
  100% { transform: scale(1)   rotate(0deg);  opacity: 1; }
}
```
Max duration: 0.35 s (TikTok), 0.4 s (others).

### checkIn
Softer pop for confirmation icons (✓).
```css
@keyframes checkIn {
  0%   { transform: scale(0) rotate(-25deg); opacity: 0; }
  65%  { transform: scale(1.2) rotate(5deg);  opacity: 1; }
  100% { transform: scale(1)   rotate(0deg);  opacity: 1; }
}
```

## Data animations

### countUp (JS)
For all numeric metrics. Reset to 0 on every `trigger(n)` call.
```javascript
function cntUp(el, dur) {
  const t = parseFloat(el.dataset.target), sf = el.dataset.suffix || '';
  const inc = t / (dur / 16); let v = 0;
  const tid = setInterval(() => {
    v = Math.min(v + inc, t);
    el.textContent = Math.floor(v) + sf;
    if (v >= t) { el.textContent = t + sf; clearInterval(tid); }
  }, 16);
}
// For decimals (e.g. $8.2B):
function cntUpDec(el, target, dur) {
  const inc = target / (dur / 16); let v = 0;
  const tid = setInterval(() => {
    v = Math.min(v + inc, target);
    el.textContent = v.toFixed(1);
    if (v >= target) { el.textContent = target.toFixed(1); clearInterval(tid); }
  }, 16);
}
```
HTML markup: `<span data-cu data-target="42" data-suffix="%">0%</span>`
Trigger in `trigger(n)`:
```javascript
s.querySelectorAll('[data-cu]').forEach(el => {
  el.textContent = '0' + (el.dataset.suffix || '');
  cntUp(el, 3000); // adjust duration per platform
});
```

### progressBar (CSS + JS)
```css
.bf { width: 0%; transition: width 2.2s cubic-bezier(.4,0,.2,1); }
```
Reset and fire in `trigger(n)`:
```javascript
const e = document.getElementById('myBar');
e.style.transition = 'none'; e.style.width = '0%';
void e.offsetWidth;            // force reflow
e.style.transition = '';
setTimeout(() => { e.style.width = '58%'; }, 600);
```

### growLine
Animated strikethrough or connector line.
```css
@keyframes growLine { from { width: 0; } to { width: 100%; } }
.sl { position: absolute; left: 0; top: 50%; height: 1.5px;
      background: var(--red); width: 0%; transform: translateY(-50%);
      border-radius: 1px; display: block; }
.slide.go .sl { animation: growLine 0.38s ease forwards; }
```

### scaleV
Vertical line growth (for architecture diagrams).
```css
@keyframes scaleV { to { transform: scaleY(1); } }
.vl { transform: scaleY(0); transform-origin: top; }
.slide.go .vl { animation: scaleV 0.28s ease forwards; }
```

### dotTravel
Moving dot along a connector (optical link animation).
```css
@keyframes dotTravel {
  0%   { left: 0%;   opacity: 0; }
  8%   { opacity: 1; }
  92%  { opacity: 1; }
  100% { left: 100%; opacity: 0; }
}
```

## Highlight & text animations

### highlightPulse
Single-pass keyword highlight. Use once per slide, on the closing key phrase.
```css
@keyframes highlightPulse {
  0%   { background: transparent; }
  38%  { background: rgba(99,102,241,.28); border-radius: 6px; padding: 0 6px; color: #fff; }
  100% { background: transparent; }
}
.pulse-active { animation: highlightPulse 2.5s ease forwards; }
```
Fire from `trigger(n)` with a delay: `setTimeout(() => el.classList.add('pulse-active'), 1300)`.

### dimText
Fade text to muted color when struck through.
```css
@keyframes dimText { to { color: var(--muted); opacity: .6; } }
```

### truthGlow
Subtle box glow for truth/confirmation cards.
```css
@keyframes truthGlow {
  0%   { box-shadow: 0 0 0 0 transparent; }
  50%  { box-shadow: 0 0 22px 5px rgba(99,102,241,.22); }
  100% { box-shadow: 0 0 0 0 transparent; }
}
```
Only use in Dark Pro style. Avoid in 小红书/X (no box-shadow rule).

## Typewriter (JS)
```javascript
let twT = null;
function typewrite(elId, word, startDelay, charDelay) {
  clearTimeout(twT);
  const el = document.getElementById(elId);
  el.textContent = '';
  let i = 0;
  const type = () => {
    if (i < word.length) { el.textContent += word[i++]; twT = setTimeout(type, charDelay); }
  };
  setTimeout(type, startDelay);
}
// Example: typewrite('tw0', 'Marvell Technology.', 1500, 90);
```

## Page transition

Use fade + subtle translate. Never full-viewport slide.
```css
.slide {
  opacity: 0;
  transform: translateY(28px);
  transition: transform 1.1s cubic-bezier(.4,0,.2,1), opacity 1.1s ease;
}
```
TikTok uses spring easing and shorter duration:
```css
.slide { transition: transform 0.6s cubic-bezier(.16,1,.3,1), opacity 0.6s ease; }
```
