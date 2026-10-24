# Imports
from flask import Flask, render_template
from database import get_all_shots, get_rounds
from analysis import practice_recommendation, performance_summary, count_clubs_used

# Create the Flask Application
app = Flask(__name__)
# Tell it what to do when someone visits the homepage
@app.route("/")
def home():
    # Send text back to the browser
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    shots = get_all_shots()
    recommendation = practice_recommendation(shots)
    total_shots = len(shots)
    rounds = get_rounds()
    total_rounds = len(rounds)
    clubs = count_clubs_used(shots)
    total_clubs = len(clubs)
    return render_template(
        "dashboard.html",
        recommendation=recommendation,
        total_shots=total_shots,
        total_rounds=total_rounds,
        total_clubs=total_clubs
    )

@app.route("/rounds")
def rounds():
    return render_template("round.html")

@app.route("/rounds/new")
def add_round_page():
    return render_template("add_round.html")

@app.route("/analysis")
def club_analysis():
    shots = get_all_shots()
    club_stats = performance_summary(shots)
    return render_template(
        "analysis.html",
        club_stats=club_stats
    )


if __name__ == "__main__":
    # Start a local development server
    app.run(debug=True)