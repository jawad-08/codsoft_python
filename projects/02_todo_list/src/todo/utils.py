from .db import get_connection

def add_task(title, description, due_date, priority):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO tasks (title, description, due_date, priority) VALUES (?, ?, ?, ?)",
            (title, description, due_date, priority),
        )
        conn.commit()

def get_tasks():
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM tasks ORDER BY due_date")
        return cur.fetchall()

def update_task_status(task_id, status):
    with get_connection() as conn:
        conn.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))
        conn.commit()

def delete_task(task_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
