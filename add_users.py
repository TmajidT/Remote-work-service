import sqlite3

def create_or_connect_to_database():
    # Database file name
    db_file = 'database.db'

    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Create or use the 'users' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY,
            First_Name TEXT,
            Last_Name TEXT,
            User_Name TEXT UNIQUE,
            Password TEXT,
            Financial_balance REAL,
            Phone_number TEXT,
            Current_city TEXT
        )
    ''')

    # Save changes and close the connection
    conn.commit()
    conn.close()

def add_user():
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Retrieve the maximum ID from the 'users' table
    c.execute('SELECT MAX(ID) FROM users')
    result = c.fetchone()
    max_id = result[0] if result[0] else 0

    # Get user information
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    user_name = input("User Name: ")
    password = input("Password: ")
    phone_number = input("Phone Number: ")
    current_city = input("Current City: ")

    # Set the initial financial balance to 0
    financial_balance = 0

    # Calculate the next user ID
    user_id = max_id + 1

    # Add user to the table
    c.execute('''
        INSERT INTO users (ID, First_Name, Last_Name, User_Name, Password, Financial_balance, Phone_number, Current_city)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, first_name, last_name, user_name, password, financial_balance, phone_number, current_city))

    # Save changes and close the connection
    conn.commit()
    conn.close()
