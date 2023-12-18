from cs50 import SQL
from datetime import datetime
from dbHelpers import createTables, categoryList, monthList
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from helpers import homeHelper, inflowHelper, loginHelper, outflowHelper, pastHelper, registerHelper

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///expenses.db")
createTables(db)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    if "username" in session.keys():
        return redirect("/home")
    else:
        return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return registerHelper(request, db)
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        return loginHelper(request, db, session)
    else:
        return render_template("login.html")

@app.route("/logout" )
def logout():
    session.clear()
    return redirect("/")

@app.route("/home", methods=["GET", "POST"])
def home():
    if "username" in session.keys():
        return homeHelper(db, session)
    else:
        redirect("/")

@app.route("/inflow", methods=["GET", "POST"])
def inflow():
    if request.method == "POST" and "username" in session.keys():
        return inflowHelper(request, db, session)
    elif "username" in session.keys():
        return render_template("inflow.html", categoryList = categoryList)
    else:
        return redirect("/")

@app.route("/outflow", methods=["GET", "POST"])
def outflow():
    if request.method == "POST" and "username" in session.keys():
        return outflowHelper(request, db, session)
    elif "username" in session.keys():
        return render_template("outflow.html", categoryList = categoryList)
    else:
        return redirect("/")

@app.route("/past", methods=["GET", "POST"])
def past():
    if request.method == "POST" and "username" in session.keys():
        return pastHelper(request, db, session)
    elif "username" in session.keys():
        current_year = datetime.now().year
        yearList = [year for year in range(current_year - 4, current_year + 1)]
        return render_template("past.html", monthList = monthList, yearList = yearList)
    else:
        return redirect("/")
