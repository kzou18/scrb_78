from flask import Flask, render_template, request, jsonify, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'James'}
    return render_template('index.html', title='Home', user=user)

@app.route("/bac_calculator")
def bac_calculator():
    return render_template("bac_calculator.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

@app.route("/stats")
def stats():
    return render_template("stats.html")
