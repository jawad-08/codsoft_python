# To-Do List App

A web-based To-Do List built with Streamlit + SQLite.

### Features
- Add, view, update, and delete tasks
- Task details: title, description, due date, priority, status
- Persistent storage using SQLite
- Interactive web UI with filters and forms

### Run
```bash
# from repo root
.\.venv\Scripts\Activate.ps1
pip install -r projects/02_todo_list/requirements.txt
streamlit run projects/02_todo_list/app.py
