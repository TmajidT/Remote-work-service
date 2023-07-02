import sqlite3

def check_user_password(user_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user_name exists in the users table
    c.execute('SELECT * FROM users WHERE User_Name = ?', (user_name,))
    result = c.fetchone()

    if result is None:
        # User_name does not exist
        print("User_name does not exist!")
        return False
    else:
        # User_name exists, prompt for password and validate it
        password = input("Password: ")

        if password == result[4]:  # result[4] is the password from the table
            print("Password is correct!")
            return True
        else:
            print("Incorrect password!")
            return False

    # Close the connection
    conn.close()


def check_operator_password(user_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user_name exists in the operators table
    c.execute('SELECT * FROM operator WHERE User_Name = ?', (user_name,))
    result = c.fetchone()

    if result is None:
        # User_name does not exist
        print("User_name does not exist!")
        return False
    else:
        # User_name exists, prompt for password and validate it
        password = input("Password: ")

        if password == result[4]:  # result[4] is the password from the table
            print("Password is correct!")
            return True
        else:
            print("Incorrect password!")
            return False

    # Close the connection
    conn.close()
