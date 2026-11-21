from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def db():
    c = sqlite3.connect("notes.db")
    c.execute("CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, text TEXT)")
    return c

@app.get("/api/notes")
def get_notes():
    return jsonify([{"id": r[0], "text": r[1]} for r in db().execute("SELECT * FROM notes")])

@app.post("/api/notes")
def add_note():
    c = db()
    c.execute("INSERT INTO notes(text) VALUES(?)", (request.json["text"],))
    c.commit()
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)