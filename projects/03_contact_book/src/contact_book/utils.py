from .db import get_connection

def add_contact(name, phone, email, address):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
            (name, phone, email, address),
        )
        conn.commit()

def get_contacts():
    with get_connection() as conn:
        cur = conn.execute("SELECT * FROM contacts ORDER BY name")
        return cur.fetchall()

def update_contact(contact_id, name, phone, email, address):
    with get_connection() as conn:
        conn.execute(
            "UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
            (name, phone, email, address, contact_id),
        )
        conn.commit()

def delete_contact(contact_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
