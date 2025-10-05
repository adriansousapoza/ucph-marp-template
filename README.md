# UCPH Marp Template

This repository contains a [Marp](https://marp.app/) presentation template based on the official design guide of the University of Copenhagen (UCPH/KU). Create professional, branded slides using simple Markdown syntax.

## Features

✅ **UCPH Branding**: Official colors, fonts, and logos  
✅ **Custom Theme**: Pre-styled with UCPH red (#901a1E) and Adobe Garamond Pro  
✅ **Header/Footer**: Automatic logo, text, and page numbers  
✅ **Video Support**: Full-screen intro videos with black/white backgrounds  
✅ **Title Pages**: Branded title slides with UCPH background  
✅ **Easy to Use**: Write slides in Markdown, export to PDF/HTML/PPTX  

## Prerequisites

### Required
- [Visual Studio Code](https://code.visualstudio.com/)
- [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/adriansousapoza/ucph-marp-template.git
cd ucph-marp-template
```

### 2. Open in VS Code

Open the `ucph-marp-template` folder in VS Code:

```bash
code .
```

Or use **File → Open Folder** in VS Code.

> **Important!** 
>
> If you prefer working from a different folder/workign directory you have to copy the `.vscode/settings.json` file into the working directory and change the location of the css file: 
> ```json
>   "markdown.marp.themes": [
>     "./[new_working_directory]/themes/ucph.css"
>   ],
> ```
> Otherwise marp won't be able to detect the .css file and the uch theme cannot be loaded.

### 3. Install Marp Extension

If you haven't already:
1. Open the Extensions panel (`Ctrl+Shift+X` or `Cmd+Shift+X`)
2. Search for "Marp for VS Code"
3. Click **Install**



### 4. Start Creating

Open `ucph.md` and start editing! The Marp extension will automatically preview your slides.

- **Preview**: Press `Ctrl+Shift V`
- **Export**: Click the Marp icon in the top-right corner → Export Slide Deck → Choose format (PDF, HTML, PPTX, PNG)



## Key Files

- **`ucph.md`**: Your presentation slides in Markdown format
- **`themes/ucph.css`**: The UCPH theme stylesheet (customizable)
- **`.vscode/settings.json`**: VS Code configuration to load the theme
- **`ucph_documents/`**: UCPH branding assets (logos, fonts, videos, colors)

## Writing Slides

### Basic Slide Structure

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






## Resources

- [Marp Official Documentation](https://marpit.marp.app/)
- [Marp for VS Code Extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
- [UCPH Design Guide](https://designguide.ku.dk/)
- [Marpit Theme CSS Documentation](https://marpit.marp.app/theme-css)

## Contributing

Contributions are welcome! Please open an issue or pull request for:
- Bug fixes
- Theme improvements
- New themes
- Documentation updates
- New slide templates

## License

This template uses UCPH branding assets. Please ensure compliance with [University of Copenhagen's brand guidelines](https://designguide.ku.dk/) when using this template.
