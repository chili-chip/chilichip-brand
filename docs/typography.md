# Typography

Four fonts, each with one job. All are free to use on the web ([SIL Open Font License](https://openfontlicense.org/)).

!!! note "The fonts may change"
    A new font is being chosen in [chilichip-brand #2](https://github.com/chili-chip/chilichip-brand/issues/2). The tokens keep today's fonts until then. Products that use `--cc-font-*` get the new font with one change.

## Fonts

<div class="cc-specimen">
<p style="font-family: var(--cc-font-display); font-weight: 800; font-size: 2.6rem">Make a game tonight</p>
<small><strong>Display: Syne 800</strong> · <code>--cc-font-display</code> · Headlines, product names, big numbers. Short lines only.</small>
</div>

<div class="cc-specimen">
<p style="font-family: var(--cc-font-text); font-size: 1rem; line-height: 1.5">The chilichip console is a pocket video game console. It comes with a creator, so you can make your own games without code and play them the same evening.</p>
<small><strong>Text: Inter 400 / 600</strong> · <code>--cc-font-text</code> · Long reading: blog posts, docs, descriptions.</small>
</div>

<div class="cc-specimen">
<p style="font-family: var(--cc-font-mono); font-size: 0.9rem; line-height: 1.5">ADD TO CART · 128×128 px · v1.2.0 · €99.00</p>
<small><strong>Mono: IBM Plex Mono 400 / 500</strong> · <code>--cc-font-mono</code> · The voice of the apps: buttons, labels, tables, prices, code.</small>
</div>

<div class="cc-specimen">
<p style="font-family: var(--cc-font-pixel); font-size: 0.9rem; line-height: 1.6">PRESS START</p>
<small><strong>Pixel: Press Start 2P</strong> · <code>--cc-font-pixel</code> · Decoration only: a score, a tag, a game title. Never for sentences.</small>
</div>

| Font | Weights to load | Source | Licence |
| --- | --- | --- | --- |
| [Syne](https://fonts.google.com/specimen/Syne) | 700, 800 | Google Fonts | OFL 1.1 |
| [Inter](https://fonts.google.com/specimen/Inter) | 400, 600 | Google Fonts | OFL 1.1 |
| [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono) | 400, 500 | Google Fonts | OFL 1.1 |
| [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) | 400 | Google Fonts | OFL 1.1 |

Host the font files yourself in products (Chili Platform already does). It is faster and sends no data to Google.

## Which font where

| Product | Headings | Body | Controls and labels |
| --- | --- | --- | --- |
| Website and blog | Display | Text | Mono |
| Docs sites | Display | Text | Mono |
| Chili Platform, Chili Creator | Display | Mono | Mono |
| Console | Console font | Console font | Console font |

The console does not use these fonts. It has its own 8 px bitmap font. See [Small screens](small-screens.md#type).

## Sizes

| Token | Size | Use | Sample |
| --- | --- | --- | --- |
| `--cc-text-3xl` | 2 to 3.2 rem | Landing page headline | <span style="font-family: var(--cc-font-display); font-weight: 800; font-size: 2rem; line-height: 1">Spicy</span> |
| `--cc-text-2xl` | 1.6 to 2.2 rem | Page title | <span style="font-family: var(--cc-font-display); font-weight: 800; font-size: 1.6rem; line-height: 1">Spicy</span> |
| `--cc-text-xl` | 1.4 rem | Section title | <span style="font-family: var(--cc-font-display); font-weight: 800; font-size: 1.4rem; line-height: 1">Spicy</span> |
| `--cc-text-lg` | 1.2 rem | Card title, lead text | <span style="font-size: 1.2rem">Spicy</span> |
| `--cc-text-md` | 1 rem | Body | <span style="font-size: 1rem">Spicy</span> |
| `--cc-text-sm` | 0.85 rem | Buttons, inputs, tables | <span style="font-family: var(--cc-font-mono); font-size: 0.85rem">Spicy</span> |
| `--cc-text-xs` | 0.75 rem | Labels, hints | <span style="font-family: var(--cc-font-mono); font-size: 0.75rem">Spicy</span> |
| `--cc-text-2xs` | 0.68 rem | Badges | <span style="font-family: var(--cc-font-mono); font-size: 0.68rem">SPICY</span> |
| `--cc-text-3xs` | 0.58 rem | Pixel font only | <span style="font-family: var(--cc-font-pixel); font-size: 0.58rem">SPICY</span> |

The two largest sizes grow with the window (`clamp`). Body text is never smaller than `--cc-text-sm`.

## Line height and spacing

| Token | Value | Use |
| --- | --- | --- |
| `--cc-leading-tight` | 1.2 | Headings, buttons |
| `--cc-leading-normal` | 1.5 | Interface text |
| `--cc-leading-loose` | 1.65 | Long reading |
| `--cc-tracking-label` | 0.08em | Upper case labels and buttons |
| `--cc-tracking-wide` | 0.12em | Badges and very small upper case text |

## Rules

| Do | Do not |
| --- | --- |
| Write headings in sentence case. | Write Headings In Title Case. |
| Use upper case for short labels and buttons only. | Set a whole sentence in upper case. |
| Keep lines of body text to 60 to 75 characters. | Let text run the full width of a wide screen. |
| Align text left. | Centre more than two lines. Justify. |
| Use one display headline per screen. | Use Syne for body text. |
