from flask import Flask, request, jsonify
import sqlite3
def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/")
def home():
    return "StudyFlow backend is running"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    task_list = []
    for task in tasks:
        task_list.append({
            "id": task["id"],
            "title": task["title"]
        })

    return jsonify(task_list)




def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)