categoryList = ["Inflow", "Food and Beverages", "Clothing", "Electronics", "Home and Furniture",
                "Health and Beauty", "Sports and Outdoors", "Books and Stationery",
                "Toys and Games", "Automotive", "Pet Supplies", "Home Improvement"]
monthList = { "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
             "August": 8, "September": 9, "October": 10, "November": 11, "December": 12 }

def createTables(db):
    db.execute("""CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            cash NUMERIC DEFAULT 0
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            description TEXT NOT NULL,
            amount NUMERIC NOT NULL,
            type TEXT NOT NULL,
            date INTEGER NOT NULL,
            month INTEGER NOT NULL,
            year INTEGER NOT NULL,
            user_username TEXT REFERENCES users(username)
    )""")
