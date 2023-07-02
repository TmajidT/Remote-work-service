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

    create_or_connect_to_database()
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

    # Get user_name from the user
    while True:
        user_name = input("User Name: ")

        # Check if the user_name already exists in the table
        c.execute('SELECT User_Name FROM users WHERE User_Name = ?', (user_name,))
        result = c.fetchone()

        if result:
            print("This User Name already exists. Please choose a different User Name.")
        else:
            break

    password = input("Password: ")

    # Get phone_number from the user
    while True:
        phone_number = input("Phone Number: ")

        if len(phone_number) != 11 or not phone_number.startswith("09"):
            print("Phone Number must be 11 digits and start with '09'.")
        else:
            break

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