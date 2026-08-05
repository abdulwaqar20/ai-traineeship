import sqlite3
import json

DB_NAME = "chat.db"

def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS messages
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT
        )
        """
    )
    connection.commit()
    connection.close()

def save_message(role, content):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages(role, content)
        VALUES (?,?)
        """,
        (
            role,
            content
        )
    )
    connection.commit()
    connection.close()

def load_messages():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT role, content
        FROM messages
        ORDER BY id
        """
    )
    rows = cursor.fetchall()
    connection.close()
    messages = []
    for role, content in rows:
        messages.append(
            {
                "role":role,
                "content":content
            }
        )
    return messages

def clear_memory():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM messages"
    )

    connection.commit()

    connection.close()