# Space, shape and motion

## Space

All gaps come from one scale with a base of 4 px. Pick a step; do not invent values.

| Token | Value | Pixels | | Typical use |
| --- | --- | --- | --- | --- |
| `--cc-space-1` | 0.25 rem | 4 | <span class="cc-bar" style="width: 4px"></span> | Icon to label |
| `--cc-space-2` | 0.5 rem | 8 | <span class="cc-bar" style="width: 8px"></span> | Inside badges, between related items |
| `--cc-space-3` | 0.75 rem | 12 | <span class="cc-bar" style="width: 12px"></span> | Button and input padding |
| `--cc-space-4` | 1 rem | 16 | <span class="cc-bar" style="width: 16px"></span> | Default gap |
| `--cc-space-5` | 1.25 rem | 20 | <span class="cc-bar" style="width: 20px"></span> | Card padding |
| `--cc-space-6` | 1.5 rem | 24 | <span class="cc-bar" style="width: 24px"></span> | Between cards |
| `--cc-space-8` | 2 rem | 32 | <span class="cc-bar" style="width: 32px"></span> | Between groups |
| `--cc-space-10` | 2.5 rem | 40 | <span class="cc-bar" style="width: 40px"></span> | Top of a page |
| `--cc-space-12` | 3 rem | 48 | <span class="cc-bar" style="width: 48px"></span> | Between sections |
| `--cc-space-16` | 4 rem | 64 | <span class="cc-bar" style="width: 64px"></span> | Between big sections |

Things that belong together sit close. Things that do not get at least twice the gap.

On the console the same idea uses whole pixels: 2, 4, 8 and 16. See [Small screens](small-screens.md#grid).

## Shape

The logo has no curves, so the interface has none either.

| Token | Value | Use |
| --- | --- | --- |
| `--cc-radius-none` | 0 | Everything: buttons, cards, inputs, images. |
| `--cc-radius-pill` | 999px | Only for things that are round by nature: avatars, on/off switches, status dots. |

Borders are 1 px in the `line` colour. A 2 px border is for focus and for the selected item.

## Depth

The logo looks solid because a lit face sits next to a shaded face. The interface does the same with flat tones. There is no blur and there are no gradients.

<div class="cc-demo">
<button class="cc-btn">Hard shadow</button>
<div class="cc-card" style="max-width: 14rem"><p class="cc-card__title">Card</p><p class="cc-card__meta">A faint red offset shadow.</p></div>
</div>

| Token | Value | Use |
| --- | --- | --- |
| `--cc-shadow-button` | `4px 4px 0` in `accent-deep` | Main buttons. The button moves onto its shadow when pressed. |
| `--cc-shadow-card` | `6px 6px 0`, chili at 12% | Cards and panels. |
| `--cc-shadow-pop` | `8px 8px 0`, chili at 16% | Dialogs and menus that float. |

Shadows always fall down and to the right, like the shaded face of the logo.

| Do | Do not |
| --- | --- |
| Offset shadow with no blur. | `box-shadow: 0 8px 24px rgba(...)` |
| A darker flat tone for the shaded side. | A gradient from light to dark. |
| A 1 px border to separate surfaces. | Glass, glow or blur effects. |

## Cut corners

The logo is full of diagonal cuts. A cut corner is the loudest shape in the system. Use it for one thing per page: a hero panel, a price tag, a featured game.

<div class="cc-demo">
<div class="cc-card cc-card--cut" style="max-width: 16rem"><p class="cc-card__title">Game of the week</p><p class="cc-card__meta">One corner cut at 45°.</p></div>
</div>

```css
.featured {
  clip-path: polygon(0 0, calc(100% - var(--cc-cut-md)) 0, 100% var(--cc-cut-md), 100% 100%, 0 100%);
}
```

| Token | Value | Use |
| --- | --- | --- |
| `--cc-cut-sm` | 6px | Tags, small panels |
| `--cc-cut-md` | 12px | Cards, hero panels |

Cut the top right corner. `clip-path` also cuts off borders and shadows, so give a cut panel a filled background and no border.

## Motion

Movement is quick and plain. Things snap; they do not float.

| Token | Value | Use |
| --- | --- | --- |
| `--cc-motion-fast` | 0.12s | Hover, press, focus |
| `--cc-motion-normal` | 0.2s | Menus and dialogs opening |
| `--cc-motion-ease` | `cubic-bezier(0.2, 0.7, 0.2, 1)` | Everything: fast start, soft stop |

Respect people who turn animation off:

```css
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; animation: none !important; }
}
```
