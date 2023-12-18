from datetime import datetime
from dbHelpers import categoryList, monthList
from flask import redirect, render_template
from werkzeug.security import check_password_hash, generate_password_hash

def registerHelper(request, db):
    username = request.form.get("username").strip()
    if not username:
        return render_template("register.html", missingUsername = True)
    storedUsername = db.execute("SELECT username FROM users WHERE username = ?", username)
    if storedUsername:
        return render_template("register.html", usernameTaken = True)

    password = request.form.get("password").strip()
    if not password:
        return render_template("register.html", missingPassword = True)
    password = generate_password_hash(password)
    db.execute("INSERT INTO users(username, password) VALUES(?, ?)", username, password)

    return redirect("/login")

def loginHelper(request, db, session):
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()
    if not username or not password:
        return render_template("login.html", incorrectDetails = True)

    storedPassword = db.execute("SELECT password FROM users WHERE username = ?", username)
    if len(storedPassword) <= 0 or not check_password_hash(storedPassword[0]["password"], password):
        return render_template("login.html", incorrectDetails = True)

    session["username"] = username
    return redirect("/")

def homeHelper(db, session):
    date = datetime.now()
    year, month = date.year, date.month
    userTransactions = db.execute("SELECT description, amount, type, date, month, year FROM transactions WHERE user_username = ? AND month = ? AND year = ?", session["username"], month, year)
    userCash = db.execute("SELECT cash FROM users WHERE username = ?", session["username"])[0]["cash"]

    userCategoryAmount = db.execute("SELECT type, SUM(amount) sum FROM transactions WHERE user_username = ? AND month = ? AND year = ? GROUP BY type", session["username"], month, year)
    userCategoryAmountArray = [["Category", "Amount"]]
    totalSpending = 0
    for row in userCategoryAmount:
        if row["sum"] < 0:
            totalSpending += abs(row["sum"])
        userCategoryAmountArray.append([row["type"], abs(row["sum"])])

    return render_template("home.html", userTransactions = userTransactions, userCash = userCash, totalSpending = totalSpending, userCategoryAmountArray = userCategoryAmountArray)

def inflowHelper(request, db, session):
    description = request.form.get("description").strip()
    amount = request.form.get("amount").strip()
    category = request.form.get("category").strip()
    date = request.form.get("date").strip()
    if not description or not amount or not category or not date:
        return render_template("inflow.html", categoryList = categoryList, missingFields = True)

    year, month, date = date.split("-")
    db.execute("""INSERT INTO transactions (description, amount, type, date, month, year, user_username)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", description, amount, category, int(date), int(month), int(year), session["username"])

    cash = db.execute("SELECT cash FROM users WHERE username = ?", session["username"])[0]["cash"]
    cash += float(amount)
    db.execute("""UPDATE users SET cash = ? WHERE username = ?""", cash, session["username"])
    return redirect("/")

def outflowHelper(request, db, session):
    description = request.form.get("description").strip()
    amount = request.form.get("amount").strip()
    category = request.form.get("category").strip()
    date = request.form.get("date").strip()
    if not description or not amount or not category or not date:
        return render_template("outflow.html", categoryList = categoryList, missingFields = True)

    year, month, date = date.split("-")
    amount = -float(amount)
    db.execute("""INSERT INTO transactions (description, amount, type, date, month, year, user_username)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", description, amount, category, date, month, year, session["username"])
    
    cash = db.execute("SELECT cash FROM users WHERE username = ?", session["username"])[0]["cash"]
    cash += float(amount)
    db.execute("""UPDATE users SET cash = ? WHERE username = ?""", cash, session["username"])
    return redirect("/")

def pastHelper(request, db, session):
    selectedMonth = request.form.get("month").strip()
    selectedYear = request.form.get("year").strip()
    if not selectedMonth or not selectedYear:
        return redirect("past.html")

    userTransactions = db.execute("SELECT description, amount, type, date, month, year FROM transactions WHERE user_username = ? AND month = ? AND year = ?", session["username"], monthList[selectedMonth], selectedYear)
    if not userTransactions:
        return redirect("/past")

    userCategoryAmount = db.execute("SELECT type, SUM(amount) sum FROM transactions WHERE user_username = ? AND month = ? AND year = ? GROUP BY type", session["username"], monthList[selectedMonth], selectedYear)
    totalSpending = 0
    for row in userCategoryAmount:
        if row["sum"] < 0:
            totalSpending += abs(row["sum"])

    return render_template("past.html", userTransactions = userTransactions, totalSpending = totalSpending)
