import sqlite3
from datetime import date


def create_job_requests_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create the job_requests table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS job_requests (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_Name TEXT,
            User_Request TEXT,
            Order_Cost INTEGER,
            Starting_Date TEXT,
            Ending_Date TEXT,
            Extra_Details TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def add_job_request(user_name, user_request, order_cost, ending_date):
    create_job_requests_table()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    starting_date = date.today().strftime("%Y-%m-%d")

    c.execute('''SELECT MAX(ID) FROM job_requests''')
    result = c.fetchone()
    next_id = 1 if result[0] is None else result[0] + 1

    c.execute('''
        INSERT INTO job_requests (ID, User_Name, User_Request, Order_Cost, Starting_Date, Ending_Date, Extra_Details)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (next_id, user_name, user_request, order_cost, starting_date, ending_date, None))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


import sqlite3


def show_all_job_requests():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM job_requests''')
    rows = c.fetchall()

    print("----------------------------------------------")
    if len(rows) == 0:
        print("No job requests found.")
    else:
        print("Job Requests:")
        print()
        for row in rows:
            print("ID:", row[0])
            print("User Name:", row[1])
            print("User Request:", row[2])
            print("Order Cost:", row[3])
            print("Starting Date:", row[4])
            print("Ending Date:", row[5])
            print("Extra Details:", row[6])
            print()

    # Close the connection
    conn.close()

    # return number of rows
    return len(rows)


def see_orders():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''SELECT * FROM orders''')
    rows = c.fetchall()

    print("----------------------------------------------")
    if len(rows) == 0:
        print("No Orders found.")
    else:
        print("Orders:")
        print()
        for row in rows:
            print("ID:", row[0])
            print("User Name:", row[2])
            print("Operator Name:", row[3])
            print("Order Cost:", row[4])
            print("Starting date:", row[5])
            print("Ending Date:", row[6])
            print("User Score:", row[7])
            print()

    # Close the connection
    conn.close()
