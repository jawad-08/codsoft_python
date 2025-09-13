# 🚀 CodSoft Internship (Python Programming)

This repository contains **three Python projects** completed during my CodSoft Internship.  
All projects are built with **Streamlit** for a modern web-based UI and focus on practical problem-solving.

---

## 📂 Projects

### 🔑 01 — Password Generator
**Path:** `projects/01_password_generator`  
A secure **Password & Passphrase Generator** with options for length, symbols, excluding ambiguous characters, and entropy-based strength scoring.  

- Built with **Streamlit** for web UI  
- Includes **unit tests** (pytest)  
- Features: Copy to clipboard, passphrase generation  

👉 [Project README](projects/01_password_generator/README.md)

---

### 📝 02 — To-Do List
**Path:** `projects/02_todo_list`  
A **To-Do List App** to add, view, update, and delete tasks with persistent storage in **SQLite**.  

- Task details: Title, description, due date, priority, status  
- Update task status / delete tasks  
- Interactive Streamlit table with filters  
- (Optional export & charts to be added)  

👉 [Project README](projects/02_todo_list/README.md)

---

### 📖 03 — Contact Book
**Path:** `projects/03_contact_book`  
A **Contact Book App** to manage and store contacts securely with validation.  

- Add, view, update, and delete contacts  
- Validate phone numbers & emails  
- Export contacts to CSV  
- Persistent storage in **SQLite**  

👉 [Project README](projects/03_contact_book/README.md)

---

## 🛠 Tech Stack
- **Python 3.10+**  
- **Streamlit** → Web UI  
- **SQLite** → Persistent storage  
- **Pytest** → Unit testing (for Password Generator)  
- **Email Validator** → Contact Book validation  

---

## ▶️ Running a Project

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/codsoft_python.git
   cd codsoft_python

2. Create & activate virtual environment:
    ```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1

3. Install dependencies (example for To-Do List):
    ```bash
pip install -r projects\02_todo_list\requirements.txt

4. Run the app:
    ```bash
streamlit run projects\02_todo_list\app.py

📌 Notes

Each project folder contains its own README.md and requirements.txt.

All apps run locally via Streamlit (http://localhost:8501).

SQLite databases (*.db) are created automatically on first run.