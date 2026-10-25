# Recipe Finder — Personal Kitchen Studio

A responsive, dark monochrome Flask website using your original recipe database and `compare()` function unchanged. All styles and scripts are local; no API keys or frontend build tools needed.

## Run (Python 3.10 or newer)

Extract the ZIP, open a terminal in the `recipe-finder` folder, then run:

```sh
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS / Linux:

```sh
source .venv/bin/activate
```

Install and start:

```sh
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. Stop with Ctrl+C. If PowerShell blocks activation, use `.venv\Scripts\python -m pip install -r requirements.txt` and `.venv\Scripts\python app.py` directly.

## Use

Enter comma-separated ingredients (no quantities) and click **Find recipes** or press Enter. Example buttons run a sample search. Matches appear in descending percentage order with ingredients you have and ingredients still needed. When all listed ingredients match, expand **Cooking instructions**. For incomplete matches the server excludes instructions from the page entirely. Add newly available ingredients to the search and search again to unlock instructions.

Matching preserves the original capitalization, whitespace, and common plural normalization. It does not interpret synonyms or quantities. Results are based on each recipe's listed ingredients; instructions are preserved verbatim and may mention additional pantry items.

## Publish online with Render

1. Create a GitHub repository and upload the contents of this folder. `app.py`, `requirements.txt`, and `render.yaml` must be at the repository root. Include `templates` and `static` with their contents.
2. Sign in at https://dashboard.render.com and choose **New > Web Service**. Connect your GitHub repository.
3. Select **Python 3**. Set the build command to `pip install -r requirements.txt` and the start command to `gunicorn --bind 0.0.0.0:$PORT app:app`.
4. Choose the **Free** instance plan and create the service.
5. When the deployment is live, open the HTTPS `onrender.com` address Render gives you. That address works in Chrome on phones, tablets, and computers, even when your own computer is off.

Alternatively, create a Render Blueprint from this repository to use the included `render.yaml` settings.

Free Render web services sleep after 15 minutes of inactivity; the first request afterward can take about a minute. This ZIP is ready to deploy but has not been published to a hosting account.

## Files

- `app.py`: Flask routes and instruction visibility
- `recipes.py`: exact copy of the original database, including `compare()`
- `templates/`, `static/`: responsive interface; search works without JavaScript
- `originals/`: untouched copies of both uploaded Python files (the desktop GUI is retained for reference)
- `test_app.py`: regression checks; run `python -m unittest -v`

The built-in server is for local use. For public hosting, use a production WSGI server and configure hosting security appropriately. No original files are modified.
