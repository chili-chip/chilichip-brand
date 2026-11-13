# Components

These are reference patterns. Each one is built only from the [tokens](tokens.md). The styles are in [`assets/components.css`](assets/components.css): copy what you need into your project and adapt it. It is not a framework.

Every example is live. Hover it, press it, tab to it.

## Button

<div class="cc-demo">
<button class="cc-btn">Add to cart</button>
<button class="cc-btn cc-btn--secondary">Details</button>
<button class="cc-btn cc-btn--quiet">Cancel</button>
<button class="cc-btn" disabled>Sold out</button>
</div>

<div class="cc-demo" data-theme="light">
<button class="cc-btn">Add to cart</button>
<button class="cc-btn cc-btn--secondary">Details</button>
<button class="cc-btn cc-btn--quiet">Cancel</button>
<button class="cc-btn" disabled>Sold out</button>
</div>

```html
<button class="cc-btn">Add to cart</button>
<button class="cc-btn cc-btn--secondary">Details</button>
<button class="cc-btn cc-btn--quiet">Cancel</button>
<button class="cc-btn" disabled>Sold out</button>
```

| Kind | Use | How many |
| --- | --- | --- |
| Primary (chili) | The one thing we want people to do. | One per screen. |
| Secondary (outline) | Other real actions. | A few. |
| Quiet (text) | Cancel, back, less important links. | Any. |

| State | What changes |
| --- | --- |
| Hover | Fill goes to `accent-shade`. |
| Pressed | The button moves 4 px down and right, onto its shadow. |
| Focus | 2 px outline in `focus`, 2 px away from the button. |
| Disabled | Grey fill, no shadow. Say why nearby ("Sold out"). |

Labels are short verbs in upper case mono: "Buy", "Save game", "Sign in". The text on a chili button is always `on-accent` (near black).

## Card

<div class="cc-demo">
<div class="cc-card" style="width: 15rem">
<p class="cc-card__title">Space Fighters TURBO</p>
<p class="cc-card__meta">Arcade · 1 player · €4.00</p>
</div>
<div class="cc-card cc-card--cut" style="width: 15rem">
<p class="cc-card__title">Game of the week</p>
<p class="cc-card__meta">Cut corner: one per page.</p>
</div>
</div>

```html
<div class="cc-card">
  <p class="cc-card__title">Space Fighters TURBO</p>
  <p class="cc-card__meta">Arcade · 1 player · €4.00</p>
</div>

<div class="cc-card cc-card--cut">…</div>
```

A card is a `surface` with a 1 px `line` border and a hard shadow. Titles use the display font. Details use mono in `muted`.

## Badge

<div class="cc-demo">
<span class="cc-badge">Draft</span>
<span class="cc-badge cc-badge--accent">New</span>
<span class="cc-badge cc-badge--success">Published</span>
<span class="cc-badge cc-badge--warning">Low stock</span>
</div>

```html
<span class="cc-badge">Draft</span>
<span class="cc-badge cc-badge--accent">New</span>
<span class="cc-badge cc-badge--success">Published</span>
<span class="cc-badge cc-badge--warning">Low stock</span>
```

A badge always has a word in it, so it never depends on colour alone.

## Form field

<div class="cc-demo">
<label class="cc-field">
<span class="cc-label">Game title</span>
<input class="cc-input" value="Chili Snake">
<span class="cc-hint">Up to 40 characters.</span>
</label>
<label class="cc-field">
<span class="cc-label">Email</span>
<input class="cc-input" value="kacper@" aria-invalid="true">
<span class="cc-hint cc-hint--error">✕ This is not an email address.</span>
</label>
</div>

```html
<label class="cc-field">
  <span class="cc-label">Game title</span>
  <input class="cc-input" value="Chili Snake">
  <span class="cc-hint">Up to 40 characters.</span>
</label>
```

| Rule | Why |
| --- | --- |
| The label sits above the field and is always visible. | Placeholders vanish when you type. |
| Errors go under the field, with a mark and plain words. | Colour alone is not enough. |
| Say how to fix it, not only what is wrong. | "Use 8 or more characters", not "Invalid password". |

## Notice

<div class="cc-demo cc-demo--stack">
<div class="cc-notice"><strong>Note.</strong> Your game is saved on this device.</div>
<div class="cc-notice cc-notice--success"><strong>Published.</strong> Chili Snake is live on Chili Platform.</div>
<div class="cc-notice cc-notice--warning"><strong>Almost full.</strong> You have 28 of 30 games.</div>
<div class="cc-notice cc-notice--danger"><strong>Not saved.</strong> The file is larger than 1.5 MB.</div>
</div>

```html
<div class="cc-notice cc-notice--success"><strong>Published.</strong> Chili Snake is live on Chili Platform.</div>
```

Start with one bold word that names the state. Then one short sentence.

## Link

<div class="cc-demo">
<p style="font-family: var(--cc-font-text)">Read the <a href="#link" style="color: var(--cc-link)">creator guide</a> to make your first game.</p>
</div>

Links are `link` (leaf) and underlined in running text. Red is for actions, green is for going somewhere.

## Checklist for a new component

| Check | How |
| --- | --- |
| Only tokens, no raw colours or sizes | Search your CSS for `#` and `px`. |
| Square corners, hard shadow | See [Shape](layout.md#shape) and [Depth](layout.md#depth). |
| Works in dark and light | Wrap it in `data-theme="light"`. |
| Readable | Text roles on `bg` or `surface` only. See [Contrast](colour.md#contrast). |
| Usable with a keyboard | Tab to it. You must see the focus outline. |
| Works at 320 px wide | Shrink the window. |
