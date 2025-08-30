from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/event_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

# Home page
@app.route('/')
def home():
    events = Event.query.all()
    return render_template('home.html', events=events)

# Create event
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        location = request.form['location']
        new_event = Event(name=name, date=date, location=location)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html')

# Event details / register
@app.route('/details/<int:event_id>', methods=['GET', 'POST'])
def details(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        registration = Registration(name=name, email=email, event_id=event.id)
        db.session.add(registration)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('details.html', event=event)

# Admin page
@app.route('/admin')
def admin():
    events = Event.query.all()
    registrations = Registration.query.all()
    return render_template('admin.html', events=events, registrations=registrations)

# Run the app
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
