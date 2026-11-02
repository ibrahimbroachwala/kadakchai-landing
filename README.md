# kadakchai.tappstudio.in

Landing site and store-required pages for **Kadak: Idle Chai Empire** (tappStudio). Plain static HTML on GitHub Pages: no build step, no framework. Work happens on `release`, and Pages publishes `release` from the repo root.

| URL | File | Notes |
|---|---|---|
| `/` | `index.html` | Landing: the tapri street under the live sky (IST), with the sun or moon placed by the hour, a train every half minute or so, customers walking up and paying, sound (off until the speaker button is tapped), a time-of-day slider, Google Play and App Store buttons, footer with legal links |
| `/privacy-policy/` | `privacy-policy/index.html` | `noindex`, linked from the landing footer |
| `/terms/` | `terms/index.html` | `noindex`, linked from the landing footer |
| `/support/` | `support/index.html` | `noindex`, also the data-deletion page (`/support/#3-data-deletion`) |

The old `tappstudio.in/kadak/*.html` URLs redirect here.

## Local preview

```bash
python3 -m http.server 8124
```

Add `?h=21` (any hour 0–24) to the landing URL to see the sky at that time of day in India, or drag the slider above the footer ("Live" goes back to the real time).

## Editing the legal pages

Edit the Markdown in `legal-src/`, then regenerate the HTML (needs `pip install markdown`):

```bash
python3 tools/build_legal.py
```

## Where things come from

- The street (skyline, train, tapri, bench, lamp, cycle) is the App Store header video's, `store/creative/src/video/header/index.html` in the Kadak game repo, in the same hero units; the sky keyframes and Pital palette are from `docs/pital-specimen.html` there; the customers follow `lib/features/tapri/presentation/widgets/street_customers.dart` (walk in from the edge, wait 1.4 s, get served at 0.8 s, walk off).
- `assets/art/` holds Bablu Bhaiya's two faces (`design/art/ustaad/`) and the kettle (`store/creative/src/app/art/`); `assets/audio/` is the game's `assets/audio/` (street ambience, music loop, pour, coin, clink, train horn). The train's wheel clatter is synthesised in the page.
- `assets/icon-512.png` is the game's `assets/icon/app_icon_512.png`; the favicon and touch icon are resized from it.

## Hosting

- `CNAME` holds `kadakchai.tappstudio.in`. DNS: a `CNAME` record `kadakchai` → `ibrahimbroachwala.github.io` at the tappstudio.in DNS provider.
- `.nojekyll` turns off Jekyll, so `legal-src/` and `tools/` are served as plain files (they hold nothing secret).
