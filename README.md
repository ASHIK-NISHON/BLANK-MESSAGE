# Braille Blanks Generator

![App screenshot](screenshot.png)

Ever seen a comment that's... nothing? ✨
You scroll through the comments, and there it is—a line that looks completely blank, yet it somehow exists. It's not a glitch. It's not magic. It's the power of the Braille Pattern Blank (U+2800), an invisible Unicode character that creates empty-looking space.

This Windows tool lets you generate as much of this "invisible ink" as you want. Create blocks of seemingly empty lines to test UI layouts, create quirky social media posts, or simply enjoy the art of nothingness. Copy and paste the void with a single click.


## Highlights

- Generate any number of invisible-looking lines (customizable).
- View results in a scrollable GUI and copy the block to the clipboard.
- Single-file Python app.

- ## Clone the Repository

```bash
git clone https://github.com/ASHIK-NISHON/BLANK-MESSAGE
cd BLANK-MESSAGE
```

## Requirements (Windows)

- Windows 10 or newer.
- Python 3.7 or newer (installed on Windows).
- `tkinter` (included with standard Windows Python installers).
- `pyperclip` (for clipboard functionality).

## Install (Windows)

Open PowerShell and run:

```powershell
python -m pip install --upgrade pyperclip
```

Notes:
- On standard Windows Python installs, `tkinter` is included. If you installed Python from the Microsoft Store or a minimal distribution, ensure you included the Tkinter feature.

## Run

Run the script (default filename `blank.py`) from the folder containing it:

```bash
python blank.py
```

This opens a small GUI where you can set how many lines to generate, preview them, copy to clipboard, or clear the output.

## Quick usage

1. Enter a positive integer for the number of lines (default is 1000).
2. Click "Generate Braille Blanks" to populate the text area.
3. Click "Copy to Clipboard" to copy the generated content.
4. Click "Clear" to remove the content.

## Troubleshooting (Windows)

- `ModuleNotFoundError: No module named 'pyperclip'` — run the pip install command above.
- If clipboard copy fails, verify that other clipboard operations in Windows work and try restarting the app.
- If the GUI does not appear, confirm your Python installation includes `tkinter` (install the official Python installer from python.org and enable the Tk/Tcl option).

## License

Public domain / use freely. No warranty.

---
