# Portfolio — Muhammad Waseem Hanif

Single-page client-facing portfolio. Static HTML, no build step, no JavaScript.

Live: published as a Claude Artifact (private until shared from the page's share menu).

## Layout

```
index.html              the whole page - semantic HTML + inline CSS
assets/                 generated images - do NOT hand-edit
scripts/build_assets.py rebuilds assets/ from the original project folders
```

## Rebuilding the images

```
python scripts/build_assets.py
```

Reads from the original project folders (thesis maps, ParcelAI figures, lunar
outputs, Fiverr gallery cards, LinkedIn poster previews) and writes optimized
copies into `assets/`. It never modifies a source file. It prints every output
size and fails if any file exceeds the 15 MB artifact limit.

PDF cover thumbnails are skipped unless PyMuPDF is installed (`pip install
pymupdf`); without it the sample section falls back to a typographic card,
which is what is currently shipped.

## Republishing

Ask Claude to republish `index.html` in the same conversation and it keeps the
same URL. From a new conversation, the artifact URL has to be passed explicitly
or a second, separate artifact gets created.

## Putting it on GitHub Pages

The artifact sandbox blocks file downloads, so the two sample PDFs are
request-by-email links. A GitHub Pages copy fixes that and gives a permanent URL:

1. Create a public repo under the `MW-Font` account.
2. Copy `index.html` and `assets/` into it.
3. Copy the two sample PDFs from `D:\Workspace\me\fiverr\` into `assets/` and
   change the two "Request the full document" links to point at them.
4. Settings -> Pages -> deploy from branch `main`, folder `/ (root)`.

## Content rules

These are deliberate and should survive future edits:

- No testimonials, client counts or "projects delivered" figures. None exist.
- Credentials are **BSc (Hons) Space Science**. Never MSc.
- No trading performance, win-rate or profitability claims. Demo accounts only.
- The Acta Geophysica manuscript is **drafted**, not submitted and not accepted.
- The AI Receptionist is **in design** - no implementation exists.
- No YouTube channel names and no footage sources anywhere on the page.
- The light-pollution entry credits the third-party base platform.
- ParcelAI is R&D in progress; blind automation is explicitly not claimed.

## Known gaps

- No GeoReport AI screenshot exists; that card uses a pipeline diagram instead.
- No FGT app screenshots exist; that card uses the app icon.
- No Beast web app screenshot exists.
- LinkedIn button is not on the page yet - the profile URL was never supplied.
