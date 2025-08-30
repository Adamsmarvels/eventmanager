from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize database (with tickets)
conn = sqlite3.connect("events.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                date TEXT,
                time TEXT,
                tickets INTEGER DEFAULT 0
            )""")
conn.commit()
conn.close()

@app.route("/")
def home():
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events")
    events = c.fetchall()
    conn.close()
    return render_template("home.html", events=events)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        time = request.form["time"]

        conn = sqlite3.connect("events.db")
        c = conn.cursor()
        c.execute("INSERT INTO events (title, description, date, time) VALUES (?, ?, ?, ?)",
                  (title, description, date, time))
        conn.commit()
        conn.close()

        return redirect(url_for("home"))
    return render_template("create.html")

@app.route("/event/<int:event_id>")
def event_details(event_id):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE id = ?", (event_id,))
    event = c.fetchone()
    conn.close()
    if event:
        return render_template("details.html", event=event)
    else:
        return "<h1>Event not found</h1>", 404

@app.route("/register/<int:event_id>")
def register(event_id):
    conn = sqlite3.connect("events.db")
    c = conn.cursor()
    c.execute("UPDATE events SET tickets = tickets + 1 WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()
    return redirect(f"/event/{event_id}")

if __name__ == "__main__":
    app.run(debug=True)