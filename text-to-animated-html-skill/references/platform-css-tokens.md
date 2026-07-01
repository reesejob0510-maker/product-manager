# Platform CSS Tokens

Ready-to-paste CSS variable blocks. Copy the matching block into the `<style>` section.

## 小红书 — 温润笔记

```css
:root {
  --bg:       #FAFAF8;
  --stage:    #E8E3DB;
  --card:     #F5F0EA;
  --border:   #E2DAD0;
  --text:     #1A1A1A;
  --dim:      #6B6B6B;
  --muted:    #ABABAB;
  --accent:   #E95C4B;
  --accent-s: rgba(233,92,75,.09);
}
html, body { background: var(--stage); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }

/* Slide card */
.slide {
  width: min(400px, 94vw);
  height: min(536px, 90dvh);
  background: var(--bg);
  border-radius: 18px;
  padding: 34px 28px 50px;
}
/* Forbidden in this style: box-shadow, text-shadow, linear-gradient, multiple accent colors */
```

## X / Twitter — 信息流卡片（深色）

```css
:root {
  --bg:      #0F1117;
  --card:    #16181C;
  --border:  rgba(255,255,255,.1);
  --text:    #E7E9EA;
  --dim:     #71767B;
  --muted:   #536471;
  --accent:  #1D9BF0;
  --accent-s: rgba(29,155,240,.12);
}
html, body { background: var(--bg); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }

.slide {
  width: min(480px, 94vw);
  aspect-ratio: 1 / 1;
  background: var(--bg);
  border-radius: 8px;
  padding: 32px 28px 44px;
}
/* Max border-radius: 8px. No decorative colored borders. */
```

## X / Twitter — 信息流卡片（浅色）

```css
:root {
  --bg:      #FFFFFF;
  --card:    #F7F9F9;
  --border:  #CFD9DE;
  --text:    #0F1419;
  --dim:     #536471;
  --muted:   #8B98A5;
  --accent:  #1D9BF0;
  --accent-s: rgba(29,155,240,.10);
}
```

## TikTok — 竖版爆款

```css
/* Choose ONE accent color for the entire file */
:root {
  --bg:      #0A0A0A;
  --text:    #FFFFFF;
  --dim:     rgba(255,255,255,.7);
  --muted:   rgba(255,255,255,.4);
  --border:  rgba(255,255,255,.12);

  /* Pick one: */
  --accent:  #00F5FF;  /* 电光青 */
  /* --accent: #FF2D55; */  /* 热粉 */
  /* --accent: #FF9500; */  /* 金橙 */
  /* --accent: #39FF14; */  /* 荧光绿 */
}
html, body { background: var(--bg); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }

.slide {
  width: min(390px, 94vw);
  height: 100dvh;
  background: var(--bg);
  padding: 60px 32px 80px;
  display: flex; flex-direction: column; justify-content: center;
}
/* Forbidden: gradient text, multiple accent colors, any animation step > 1s */
```

## Dark Pro — 暗黑专业

```css
:root {
  --bg:      #090d18;
  --card:    #0f1626;
  --card2:   #141c2e;
  --border:  rgba(99,102,241,.18);
  --accent:  #6366f1;
  --accent2: #818cf8;
  --green:   #10b981;
  --amber:   #f59e0b;
  --red:     #ef4444;
  --text:    #f1f5f9;
  --dim:     #94a3b8;
  --muted:   #64748b;
}
html, body { background: var(--bg); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }

.deck { position: fixed; inset: 0; }
.slide { position: absolute; inset: 0; padding: 44px 24px 64px; }
.slide-inner { width: 100%; max-width: 540px; margin: 0 auto; }
```
