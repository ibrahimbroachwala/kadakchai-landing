# kadakchai.tappstudio.in

Teaser site and store-required pages for **Kadak: Idle Chai Empire** (tappStudio). Plain static HTML on GitHub Pages: no build step, no framework. Work happens on `release`, and Pages publishes `release` from the repo root.

| URL | File | Notes |
|---|---|---|
| `/` | `index.html` | Teaser: the tapri under the live sky (IST), customers walking up and paying, the "Jald aa rha hai" board |
| `/privacy-policy/` | `privacy-policy/index.html` | `noindex`, not linked from the teaser |
| `/terms/` | `terms/index.html` | `noindex`, not linked from the teaser |
| `/support/` | `support/index.html` | `noindex`, also the data-deletion page (`/support/#3-data-deletion`) |

The old `tappstudio.in/kadak/*.html` URLs redirect here.

## Local preview

```bash
python3 -m http.server 8124
```

Add `?h=21` (any hour 0–24) to the teaser URL to see the sky at that time of day in India.

## Editing the legal pages

Edit the Markdown in `legal-src/`, then regenerate the HTML (needs `pip install markdown`):

```bash
python3 tools/build_legal.py
```

## Where things come from

- The tapri, sky keyframes and Pital palette are from `docs/pital-specimen.html` in the Kadak game repo; the customers follow `lib/features/tapri/presentation/widgets/street_customers.dart` (walk in from the edge, wait 1.4 s, get served at 0.8 s, walk off).
- `assets/icon-512.png` is the game's `assets/icon/app_icon_512.png`; the favicon and touch icon are resized from it.

## Hosting

- `CNAME` holds `kadakchai.tappstudio.in`. DNS: a `CNAME` record `kadakchai` → `ibrahimbroachwala.github.io` at the tappstudio.in DNS provider.
- `.nojekyll` turns off Jekyll, so `legal-src/` and `tools/` are served as plain files (they hold nothing secret).
