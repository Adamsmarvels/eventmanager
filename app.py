from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client
import os

app = Flask(__name__)

# ------------------------------
# Supabase connection
# ------------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# ------------------------------
# Routes
# ------------------------------

# Home page - list all events
@app.route("/")
def home():
    events = supabase.table("events").select("*").execute().data
    return render_template("home.html", events=events)


# Create a new event
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        date = request.form["date"]
        time = request.form["time"]

        supabase.table("events").insert({
            "name": title,
            "description": description,
            "date": date,
            "time": time
        }).execute()

        return redirect(url_for("home"))
    return render_template("create.html")


# Event details + register
@app.route("/details/<int:event_id>", methods=["GET", "POST"])
def details(event_id):
    # Get event details
    event = supabase.table("events").select("*").eq("id", event_id).single().execute().data

    # Count registrations
    reg_data = supabase.table("registrations").select("*").eq("event_id", event_id).execute().data
    num_tickets = len(reg_data)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        supabase.table("registrations").insert({
            "name": name,
            "email": email,
            "event_id": event_id
        }).execute()
        return redirect(url_for("home"))

    return render_template("details.html", event=event, num_tickets=num_tickets)


# Admin page - list all events and registrations
@app.route("/admin")
def admin():
    events = supabase.table("events").select("*").execute().data
    registrations = supabase.table("registrations").select("*").execute().data
    return render_template("admin.html", events=events, registrations=registrations)


# ------------------------------
# Run locally
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
