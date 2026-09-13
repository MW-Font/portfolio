# Portfolio — Muhammad Waseem Hanif

Live: https://mw-font.github.io/portfolio/

AI systems and automation work, with satellite remote sensing as the
measurement background. Static, no build tooling, no dependencies.

## Layout

```
src/page.html           SOURCE. Edit this one.
index.html              GENERATED for GitHub Pages. Do not hand-edit.
scripts/build_page.py   wraps the source in a real document shell
scripts/build_assets.py rebuilds assets/ from the original project folders
assets/                 generated images. Do not hand-edit.
assets/raw/             source screenshots, gitignored
```

**Why two HTML files.** `src/page.html` is authored for the Claude Artifact
host, which supplies its own `<!doctype>`/`<head>`/`<body>` at publish time.
GitHub Pages serves files raw, so the same markup needs a document shell around
it, above all a viewport meta: without one, phones render at desktop width.

## Editing

1. Edit `src/page.html`.
2. Run `python scripts/build_page.py` to regenerate `index.html`.
3. Commit and push. Pages redeploys in about a minute.

The email button adapts to where it is served: inside an iframe it copies the
address to the clipboard, because that sandbox blocks `mailto:` handoff. Served
top-level, it is promoted to a real mail link.

## Rebuilding images

```
python scripts/build_assets.py
```

Reads from the original project folders and writes optimized copies into
`assets/`. It never modifies a source file, prints every output size, and fails
if any file exceeds 15 MB.

## Content rules

Deliberate, and they should survive future edits:

- No testimonials, client counts or "projects delivered" figures. None exist.
- Credentials are **BSc (Hons) Space Science**. Never MSc.
- No trading performance, win-rate or profitability claims. Demo accounts only.
- The Acta Geophysica manuscript is **drafted**, not submitted, not accepted.
- No YouTube channel names and no footage sources anywhere on the page.
- The light-pollution entry credits the third-party base platform.
- ParcelAI is R&D in progress; blind automation is explicitly not claimed.
- Private repositories are described as private, not linked as if browsable.
