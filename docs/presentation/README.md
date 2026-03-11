# Capstone Presentation

`presentation.md` is a [Marp](https://marp.app/) markdown slide deck.

## Rendering to PDF or PPTX (recommended for Zoom)

Install the Marp CLI once:

```bash
npm install -g @marp-team/marp-cli
```

Then from this folder:

```bash
# Export to PDF
marp presentation.md --pdf --allow-local-files -o presentation.pdf

# Export to PowerPoint
marp presentation.md --pptx --allow-local-files -o presentation.pptx

# Export to HTML (self-contained, can share the file)
marp presentation.md --html --allow-local-files -o presentation.html
```

## Live preview in VS Code / Cursor

Install the **Marp for VS Code** extension, then open `presentation.md` and click the
preview button in the top-right corner.

## Slide count and timing

| Slides | Target time |
|---|---|
| 19 slides | ~20 minutes |

Each slide has a `<!-- SCRIPT -->` comment block with the exact text to read aloud.
These comments are not visible in the rendered output.
