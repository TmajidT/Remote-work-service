import sqlite3


def add_operator():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS operator (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            First_Name TEXT,
            Last_Name TEXT,
            User_Name TEXT UNIQUE,
            Password TEXT,
            Phone_number TEXT,
            Active_city TEXT,
            Financial_balance INTEGER DEFAULT 0,
            Average_points REAL DEFAULT NULL
        )
    ''')

    # Get user input for operator details
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    # Check if the entered User_Name already exists
    while True:
        user_name = input("User Name: ")
        c.execute("SELECT User_Name FROM operator WHERE User_Name=?", (user_name,))
        result = c.fetchone()
        if result is None:
            break
        else:
            print("This User Name is already taken. Please enter a different User Name.")

    password = input("Password: ")

    # Validate and get a 11-digit phone number
    while True:
        phone_number = input("Phone Number: ")
        if len(phone_number) == 11 and phone_number.startswith("09"):
            break
        else:
            print("Invalid phone number. Please enter an 11-digit phone number starting with '09'.")

    active_city = input("Active City: ")

    # Insert the operator details into the table
    c.execute(
        "INSERT INTO operator (First_Name, Last_Name, User_Name, Password, Phone_number, Active_city) VALUES (?, ?, ?, ?, ?, ?)",
        (first_name, last_name, user_name, password, phone_number, active_city))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()