# UCPH Marp Template

A [Marp](https://marp.app/) presentation template based on the official design guide of the University of Copenhagen (UCPH/KU). Create professional, branded slides using simple Markdown syntax.

---

## Getting Started

### 1. Install Marp

Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension (recommended) or the [Marp CLI](https://marp.app/#get-started).

> This template was developed for the **Marp for VS Code** extension but is also compatible with the **Marp CLI**.

### 2. Clone this repository

```bash
git clone https://github.com/adriansousapoza/ucph-marp-template.git
cd ucph-marp-template
code .
```

Or use **File → Open Folder** in VS Code.

> **Important — theme loading and workspace roots**
> The Marp for VS Code extension only reads `.vscode/settings.json` from the folder you actually open (`File → Open Folder`). If you open a *parent* folder instead of `ucph-marp-template` itself, this repo's `.vscode/settings.json` is invisible to VS Code, so the `ucph` theme is never registered — even though `presentation.md` and `themes/ucph.css` are still sitting right next to each other. (The setting is also resolved relative to whatever folder *is* open, not relative to the `.md` file, so a copied/relative path wouldn't help either — see [marp-vscode#themes.ts](https://github.com/marp-team/marp-vscode/blob/main/src/themes.ts).)
>
> **Fix (one-time, per machine):** add the theme to your VS Code **User** settings (not this repo's settings) via a stable URL, so it registers no matter which folder you open:
>
> 1. `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**
> 2. Add:
>    ```json
>    "markdown.marp.themes": [
>      "https://raw.githubusercontent.com/adriansousapoza/ucph-marp-template/main/themes/ucph.css"
>    ]
>    ```
>
> This only takes effect when no workspace-level `markdown.marp.themes` is set. Opening `ucph-marp-template` directly still uses this repo's own `.vscode/settings.json` (the local `./themes/ucph.css`), so theme edits preview instantly with no internet needed in that case. Open a different parent folder instead, and the User-level remote URL takes over automatically. The only requirement stays exactly what you'd expect: `presentation.md` and the `ucph_documents/` folder need to sit in the same folder — everything else (videos, fonts, logos, background images) is already resolved relative to the `.md` file, not the workspace root.
>
> Every tag this template actually uses (`<div>`, `<video>`, `<a>`, `<img>`, …) is already in [Marp's default HTML allow list](https://github.com/marp-team/marp-core/blob/main/src/html/allowlist.ts), so `markdown.marp.html: "all"` is not required — the "YouTube Videos" slide links a static thumbnail instead of embedding a live `<iframe>`, since a real embed breaks with a YouTube "Error 153" once the deck is exported to HTML and opened as a local file (no page origin for YouTube to validate against). If you add your own slide with a tag outside the default allow list, you'll need `markdown.marp.html: "all"` for that one — same User-settings scoping trade-off as above.

### 3. Start creating

Open `presentation.md` and start editing. The Marp extension will automatically preview your slides.

Example exports are included as `presentation.pdf` and `presentation.html`.

- **Preview**: `Ctrl+Shift+V` (same as standard Markdown preview)
- **Export**: `Ctrl+Shift+P` → *Marp: Export Slide Deck*, or click the Marp icon in the top-right corner of the editor

Supported export formats: **PDF**, **HTML**, **PPTX**, **PNG**

---

## Key Files

| File / Folder | Description |
|---|---|
| `presentation.md` | Your presentation slides in Markdown |
| `themes/ucph.css` | UCPH theme stylesheet (customisable) |
| `.vscode/settings.json` | VS Code config that loads the theme |
| `ucph_documents/logos/` | Official UCPH logos (DK & EN, multiple variants) |
| `ucph_documents/videos/` | Branded intro/outro video animations |
| `ucph_documents/colors/` | Official UCPH colour palettes (RGB & CMYK) |
| `ucph_documents/font/` | Adobe Garamond Pro font files |
| `ucph_documents/powerpoint/` | Official UCPH PowerPoint templates |

---

## Writing Slides

### Basic slide structure

```markdown
---
marp: true
theme: ucph
paginate: true
header: 'Your Presentation Title'
footer: 'Optional Footer Text'
---

# First Slide

Your content here...

---

# Second Slide

Your content here...
```

### Video intro/outro slides

The template includes branded UCPH video animations for opening and closing slides. Add one of the following classes to a slide:

| Class | Description |
|---|---|
| `video_intro_white_uk` | Intro · English · white background |
| `video_intro_white_dk` | Intro · Danish · white background |
| `video_intro_black_uk` | Intro · English · black background |
| `video_intro_black_dk` | Intro · Danish · black background |
| `video_outro_white_uk` | Outro · English · white background |
| `video_outro_white_dk` | Outro · Danish · white background |
| `video_outro_black_uk` | Outro · English · black background |
| `video_outro_black_dk` | Outro · Danish · black background |

Example:

```markdown
<!-- _class: video_intro_white_uk -->

<video autoplay loop muted playsinline>
  <source src="ucph_documents/videos/intro_white_uk.mp4" type="video/mp4">
</video>
```

### Title page

```markdown
<!-- _class: title-page -->

# Your Presentation Title

## Subtitle or Additional Information

Author Name
Department · University of Copenhagen
```

---

## Resources

- [Marp Official Documentation](https://marpit.marp.app/)
- [Marp for VS Code Extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
- [Marpit Theme CSS Documentation](https://marpit.marp.app/theme-css)
- [UCPH Design Guide](https://designguide.ku.dk/)

## Contributing

Contributions are welcome! Please open an issue or pull request for:

- Bug fixes
- Theme improvements or new themes
- New slide templates
- Documentation updates

## License

This template uses UCPH branding assets. Please ensure compliance with the [University of Copenhagen's brand guidelines](https://designguide.ku.dk/) when using or distributing this template.
