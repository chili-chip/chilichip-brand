# Logo and name

## The logo

The logo is a red chili drawn with straight edges, with a green stem. It has no outline and no text.

<div class="cc-plates">
<figure class="cc-plate"><img src="../assets/chilichip-logo.svg" alt="Logo on a dark background" style="background: #07080c"><figcaption>On <code>ink-0</code></figcaption></figure>
<figure class="cc-plate"><img src="../assets/chilichip-logo.svg" alt="Logo on black" style="background: #000"><figcaption>On <code>black</code></figcaption></figure>
<figure class="cc-plate"><img src="../assets/chilichip-logo.svg" alt="Logo on a light background" style="background: #f4f1ea"><figcaption>On <code>bone</code></figcaption></figure>
<figure class="cc-plate"><img src="../assets/chilichip-logo.svg" alt="Logo on white" style="background: #fff"><figcaption>On <code>paper</code></figcaption></figure>
</div>

| File | Use |
| --- | --- |
| [`logo/chilichip-logo.svg`](https://github.com/chili-chip/chilichip-brand/blob/main/logo/chilichip-logo.svg) | The master. Use it wherever you can. |
| [`logo/logo_1024.png`](https://github.com/chili-chip/chilichip-brand/blob/main/logo/logo_1024.png) | Where SVG does not work (social profiles, some stores). |
| [`logo/logo-workspace/`](https://github.com/chili-chip/chilichip-brand/tree/main/logo/logo-workspace) | Working files. Do not use these in products. |

## How it is built

The logo has three shapes and three colours. These are the [brand colours](colour.md).

<div class="cc-demo" markdown>
<svg viewBox="0 0 256 256" width="260" role="img" aria-label="The logo with its three parts labelled">
  <image href="../assets/chilichip-logo.svg" width="256" height="256"/>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="#f4f1ea">
    <line x1="70" y1="150" x2="24" y2="92" stroke="#9aa3b5"/><text x="4" y="86">lit face #ff3030</text>
    <line x1="150" y1="170" x2="170" y2="226" stroke="#9aa3b5"/><text x="118" y="240">shaded face #e42020</text>
    <line x1="200" y1="92" x2="150" y2="40" stroke="#9aa3b5"/><text x="80" y="34">stem #2eac00</text>
  </g>
</svg>

<div style="font-family: var(--cc-font-mono); font-size: 0.75rem; max-width: 18rem">
<p>The light comes from the top left. The top of the chili is lit. The underside is one step darker.</p>
<p style="margin-top: 0.75rem; color: var(--cc-muted)">The same idea makes buttons and cards look solid: one flat tone next to a darker flat tone.</p>
</div>
</div>

## Clear space

The SVG is a 256×256 square. The chili sits inside it with a margin of about one eighth of the width on every side. That margin is the clear space.

<div class="cc-demo" markdown>
<svg viewBox="0 0 256 256" width="260" role="img" aria-label="The logo inside its square, with the margin marked">
  <rect x="0.5" y="0.5" width="255" height="255" fill="none" stroke="#9aa3b5" stroke-dasharray="4 3"/>
  <rect x="29" y="29" width="206" height="192" fill="none" stroke="#6fe33a" stroke-dasharray="2 3"/>
  <image href="../assets/chilichip-logo.svg" width="256" height="256"/>
  <g font-family="IBM Plex Mono, monospace" font-size="9" fill="#9aa3b5">
    <line x1="0" y1="128" x2="29" y2="128" stroke="#ffb347"/><text x="3" y="122" fill="#ffb347">1/8</text>
    <text x="6" y="250">256 × 256 square</text>
  </g>
</svg>

<div style="font-family: var(--cc-font-mono); font-size: 0.75rem; max-width: 18rem">
<p>Keep the whole square. Do not crop closer to the chili.</p>
<p style="margin-top: 0.75rem; color: var(--cc-muted)">Text, other logos and the edge of the page stay outside the dashed square.</p>
</div>
</div>

## Sizes

| Where | Smallest size | Which file |
| --- | --- | --- |
| Screens | 24 px wide | `chilichip-logo.svg` |
| Favicons and tiny icons | 16 px | A pixel version. See [Small screens](small-screens.md#logo). |
| The console screen | 16 px | A pixel version, drawn with hard pixels. |
| Print | 10 mm wide | `chilichip-logo.svg` |

## Backgrounds

<div class="cc-plates">
<figure class="cc-plate cc-plate--yes"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a"><figcaption>Dark neutral</figcaption></figure>
<figure class="cc-plate cc-plate--yes"><img src="../assets/chilichip-logo.svg" alt="" style="background: #f4f1ea"><figcaption>Light neutral</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #ff3030"><figcaption>Chili red: the chili is gone</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #2eac00"><figcaption>Leaf green: the stem is gone</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #ffb347"><figcaption>Other bright colours</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: repeating-linear-gradient(45deg, #262c38 0 12px, #9aa3b5 12px 24px)"><figcaption>Busy pictures and patterns</figcaption></figure>
</div>

On a photo or a pattern, put the logo on a plain dark plate (`ink-0`) first.

## Do not

<div class="cc-plates">
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; filter: hue-rotate(200deg)"><figcaption>Change the colours</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; transform: scaleX(0.6)"><figcaption>Stretch or squash</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; transform: rotate(90deg)"><figcaption>Rotate</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; filter: drop-shadow(0 0 10px #ff3030)"><figcaption>Add glow or soft shadow</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; filter: blur(1.5px)"><figcaption>Blur or use a low quality copy</figcaption></figure>
<figure class="cc-plate cc-plate--no"><img src="../assets/chilichip-logo.svg" alt="" style="background: #10131a; border-radius: 50%"><figcaption>Crop into a circle yourself</figcaption></figure>
</div>

Also do not redraw the logo, add an outline, or place text on top of it.

## The name

| Write | Not | Why |
| --- | --- | --- |
| chilichip | Chilichip, ChiliChip, Chili Chip, chilli chip | One word, always lower case, also at the start of a sentence. |
| chilichip console, the console | VGC Zero | The public name of the handheld. |
| Chili Platform, Chili Creator, Chili Beat | chili platform, ChiliPlatform | Products are two words with capitals. |

There is no drawn wordmark yet. Until there is one, set the name in Syne ExtraBold, lower case, next to the logo:

<div class="cc-demo">
<img src="../assets/chilichip-logo.svg" alt="" width="56">
<span style="font-family: var(--cc-font-display); font-weight: 800; font-size: 2rem; letter-spacing: -0.01em">chilichip</span>
</div>

<div class="cc-demo" data-theme="light">
<img src="../assets/chilichip-logo.svg" alt="" width="56">
<span style="font-family: var(--cc-font-display); font-weight: 800; font-size: 2rem; letter-spacing: -0.01em">chilichip</span>
</div>

The gap between logo and name is small because the logo already carries its own margin.

!!! note "Not decided yet"
    A drawn wordmark, a one-colour logo and hand-tuned pixel logos are open. See [Open questions](open-questions.md).
