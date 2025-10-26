# Simple Flask page with scrollable carousels

This small Flask app provides a single page with three sections (top, middle, bottom). The middle and bottom sections contain horizontally scrollable carousels where you can add "cards".

Getting started (PowerShell on Windows):

1. Create and activate a Python virtual environment (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python .\app.py
```

4. Open http://127.0.0.1:5000 in your browser.

How to add cards
- Edit the lists in `app.py` or change the view to pull data from a database. The template iterates `middle_cards` and `bottom_cards` to render each card.

Files created:
- `app.py` — Flask app entrypoint.
- `templates/index.html` — the page template with two carousels.
- `static/css/style.css` — simple styling for carousels and layout.
- `static/js/carousel.js` — JS to scroll carousels with buttons and drag.
- `requirements.txt` — dependency list.

Feel free to tell me how you'd like the cards styled or if you want server-side data loading (JSON API, DB integration, etc.).
# Game-Panel