# Contact Book

A web-based Contact Book built with Streamlit + SQLite.

### Features
- Add, view, update, and delete contacts
- Validate phone (7–15 digits) and email format
- Export contacts to CSV
- Persistent storage using SQLite
- Simple modern web UI

### Run
```bash
# from repo root
.\.venv\Scripts\Activate.ps1
pip install -r projects/03_contact_book/requirements.txt
streamlit run projects/03_contact_book/app.py
