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

> **Important**
> You must open the `ucph-marp-template` folder directly. The UCPH theme will not load if you open a parent or different directory.
>
> If you prefer a different working directory, copy `.vscode/settings.json` into it and update the theme path:
> ```json
> "markdown.marp.themes": [
>   "./themes/ucph.css"
> ]
> ```

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
