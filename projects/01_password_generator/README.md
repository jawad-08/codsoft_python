# Password Generator

A small web app (Streamlit) to generate secure passwords and passphrases.
Features:
- Generate random passwords with options: length, uppercase, lowercase, digits, symbols, exclude ambiguous chars.
- Generate passphrases (word-based) with configurable word count and separator.
- Strength estimation (entropy) and human-friendly label.
- Copy-to-clipboard button in the UI.
- Unit tests (pytest).

Run:
1. Activate venv: `.\.venv\Scripts\Activate.ps1`
2. Install deps: `pip install -r requirements.txt`
3. Run: `streamlit run projects/01_password_generator/app.py`
