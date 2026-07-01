# Slide Templates

Ready-to-use HTML snippets for common slide types. Adapt content; keep class names.

## Hook slide (slide 0)

```html
<div class="slide go" id="s0">
  <div class="slide-inner">
    <p class="tag ai d1">0:00 · 开场</p>
    <p class="hook-lead ai d2"><!-- one sentence lead-in --></p>
    <div class="super ai d3">$<span id="cu0">0</span></div>
    <p class="super-sub ai d3"><!-- unit label e.g. billion check --></p>
    <p class="sub ai d4" style="color:var(--text)"><!-- follow-up sentence --></p>
    <div class="reveal-line ai d5">
      <!-- reveal phrase --> <span id="tw0"></span><span class="cursor"></span>
    </div>
  </div>
</div>
```
JS in trigger(0):
```javascript
cntUp2(document.getElementById('cu0'), 2, 1000); // counts 0→2
typewrite('tw0', 'Brand Name.', 1500, 90);
```

## Metric card slide

```html
<div class="slide" id="sN">
  <div class="slide-inner">
    <p class="tag ai d1">0:50 · 数据</p>
    <h2 class="head ai d2">数字会说话</h2>
    <div class="mrow">
      <div class="mc-m ai d2">
        <div class="mn">$<span data-cu data-target="82" data-suffix="亿">0亿</span></div>
        <div><p class="ml">FY2026 全年营收</p><span class="mb-g">↑ +42% YoY</span></div>
      </div>
      <div class="mc-m ai d3">
        <div class="mn"><span data-cu data-target="76" data-suffix="%">0%</span></div>
        <div><p class="ml">数据中心占比</p><span class="mb-g">核心业务</span></div>
      </div>
    </div>
  </div>
</div>
```

## Myth card slide (misconception → truth)

```html
<div class="slide" id="sN">
  <div class="slide-inner">
    <p class="tag ai d1">0:08 · 误解</p>
    <h2 class="head ai d2">你以为它是…<br>其实都不是。</h2>
    <div class="myth-list">

      <div class="myth-card mc1">
        <div class="mi x mico1">✕</div>
        <div style="flex:1">
          <p class="mlbl">误解 ①</p>
          <p class="mtxt"><span class="sw"><!-- wrong belief --><span class="sl sl1"></span></span></p>
        </div>
      </div>

      <div class="myth-card mc2">
        <div class="mi x mico2">✕</div>
        <div style="flex:1">
          <p class="mlbl">误解 ②</p>
          <p class="mtxt"><span class="sw"><!-- wrong belief --><span class="sl sl2"></span></span></p>
        </div>
      </div>

      <div class="myth-card truth mc3">
        <div class="mi ok mico3">✓</div>
        <div style="flex:1">
          <p class="mlbl">真相</p>
          <p class="mt3"><!-- truth statement --></p>
        </div>
      </div>

    </div>
  </div>
</div>
```

## Speed bar slide (comparison bars)

```html
<div class="slide" id="sN">
  <div class="slide-inner">
    <p class="tag ai d1">0:22 · 技术对比</p>
    <h2 class="head ai d2"><!-- headline --></h2>
    <div class="speed-wrap ai d3">
      <div class="sr">
        <div class="sm"><span class="lbl">当前标准</span><span class="val">800G</span></div>
        <div class="st"><div class="sf lo" id="b800">800G</div></div>
      </div>
      <div class="sr">
        <div class="sm"><span class="lbl">下一代</span><span class="val">1.6T ↑ 2×</span></div>
        <div class="st"><div class="sf hi" id="b1600">1.6T</div></div>
      </div>
    </div>
  </div>
</div>
```
JS in trigger(n):
```javascript
['b800','b1600'].forEach(id => {
  const e = document.getElementById(id);
  e.style.transition = 'none'; e.style.width = '0%'; void e.offsetWidth; e.style.transition = '';
});
setTimeout(() => document.getElementById('b800').style.width = '50%', 500);
setTimeout(() => document.getElementById('b1600').style.width = '100%', 1100);
```

## Closing slide

```html
<div class="slide" id="sN">
  <div class="slide-inner">
    <p class="tag ai d1" style="text-align:center">1:22 · 结尾</p>
    <div class="cq ai d2">
      <!-- closing question with highlight -->
      所以，你<span class="hl" id="chl">到底在买哪个故事？</span>
    </div>
    <p class="sub ai d3" style="text-align:center;margin-top:20px"><!-- sub line --></p>
    <p class="disc ai d4">数据来源：<!-- source --> · 不构成投资建议</p>
  </div>
</div>
```
JS in trigger(n):
```javascript
const hl = document.getElementById('chl');
hl.classList.remove('pulse-active'); void hl.offsetWidth;
setTimeout(() => hl.classList.add('pulse-active'), 1300);
```
