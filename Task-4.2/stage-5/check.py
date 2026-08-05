import sqlite3
connection = sqlite3.connect("chat.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()


# from database import clear_memory
# clear_memory()
# print("Memory cleared")