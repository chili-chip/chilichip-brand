# Colour

Three colours come straight from the logo. A few more are derived from them so text stays readable. The rest is neutral.

## Palette

--8<-- "palette.md"

## How much of each

Use colour in about the same amounts as the logo does on a dark page.

<div style="display: flex; height: 3rem; margin: 1em 0; border: 1px solid var(--md-default-fg-color--lightest)">
<span style="flex: 80; background: #07080c"></span><span style="flex: 12; background: #ff3030"></span><span style="flex: 5; background: #e42020"></span><span style="flex: 3; background: #2eac00"></span>
</div>

| Share | Colour | Use |
| --- | --- | --- |
| Most of the page | Neutrals | Backgrounds, text, borders. |
| A little | Chili | One main action per screen, the selected item, highlights. |
| Even less | Chili shade | The darker side of a red element. Never on its own. |
| A pinch | Leaf | Links, success, focus. Small things only. |

!!! tip "Red is for one thing at a time"
    If everything is red, nothing stands out. A screen should have one red button, not five.

## Roles

Do not use the palette names in components. Use roles. A role says what a colour is for, and it changes with the theme.

--8<-- "roles.md"

The dark theme is the default: Chili Platform, Chili Creator and the console are dark. The light theme is for long reading (the website, docs) and print.

<div class="cc-demo">
<div class="cc-card" style="max-width: 16rem"><p class="cc-card__title">Dark theme</p><p class="cc-card__meta">Text on surface. <a href="#roles" style="color: var(--cc-link)">A link</a>. <span style="color: var(--cc-accent-text)">Accent text</span>.</p></div>
<button class="cc-btn">Buy</button>
<span class="cc-badge cc-badge--success">In stock</span>
<span class="cc-badge cc-badge--warning">Low</span>
</div>

<div class="cc-demo" data-theme="light">
<div class="cc-card" style="max-width: 16rem"><p class="cc-card__title">Light theme</p><p class="cc-card__meta">Text on surface. <a href="#roles" style="color: var(--cc-link)">A link</a>. <span style="color: var(--cc-accent-text)">Accent text</span>.</p></div>
<button class="cc-btn">Buy</button>
<span class="cc-badge cc-badge--success">In stock</span>
<span class="cc-badge cc-badge--warning">Low</span>
</div>

```html
<html data-theme="light">  <!-- leave the attribute out for dark -->
```

## Contrast

Every text role is checked against the page background and the card surface. The numbers are [WCAG contrast ratios](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Normal text needs 4.5:1. The build fails if a role drops below that.

--8<-- "contrast.md"

Things to remember:

| Rule | Why |
| --- | --- |
| Text on a chili fill is `on-accent` (near black), not white. | White on chili is only 3.67:1. |
| On a light page, red and green text use the `-ink` colours. | `chili` on `bone` is 3.26:1 and `leaf` is 2.65:1. Too faint. |
| Do not put `chili-shade` text on a dark page. | 4.31:1. It is a fill colour. |
| Never show state with colour alone. | Add an icon, a label or a marker. About 1 in 12 men cannot tell red from green well. |

## On the console

The console has its own short list of roles. See [Small screens](small-screens.md#colour).
