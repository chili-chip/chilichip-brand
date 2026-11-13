# chilichip-brand

The chilichip logo, merch designs and the **chilichip design system**: colours, type, shapes and logo rules, with tokens for the website, Chili Platform, Chili Creator and the chilichip console.

Docs: [brand.chilichip.eu](https://brand.chilichip.eu) (source in [`docs/`](docs/)).

![The chilichip logo](logo/logo_1024.png)

## What is here

| Path | What |
| --- | --- |
| [`logo/chilichip-logo.svg`](logo/chilichip-logo.svg) | The logo. `logo/logo-workspace/` holds working files. |
| [`merch-design/`](merch-design/) | Merch artwork. |
| [`tokens/tokens.json`](tokens/tokens.json) | The design tokens. The only file to edit when a value changes. |
| [`docs/tokens/chilichip.css`](docs/tokens/chilichip.css) | Generated CSS variables for web projects. |
| [`docs/tokens/chilichip.json`](docs/tokens/chilichip.json) | Generated JSON. |
| [`docs/tokens/chilichip.hpp`](docs/tokens/chilichip.hpp) | Generated C++ header for the console. |
| [`docs/assets/components.css`](docs/assets/components.css) | Reference components. |
| [`docs/`](docs/) | The docs site (MkDocs Material). |
| [`tools/console_mockups.py`](tools/console_mockups.py) | Draws the 128×128 example screens. |

## The three colours

| Colour | Hex | From |
| --- | --- | --- |
| chili | `#ff3030` | Lit face of the logo |
| chili-shade | `#e42020` | Shaded face of the logo |
| leaf | `#2eac00` | Stem of the logo |

## Work on it

```sh
python3 tokens/build.py                 # write the generated files
python3 -m unittest discover tokens     # check colours, contrast and that nothing is stale

pip install -r docs/requirements.txt
mkdocs serve                            # docs on http://127.0.0.1:8000
```

Pull requests run the tests and build the docs. A push to `main` deploys the docs to Cloudflare Pages.
