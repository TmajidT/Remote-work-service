import sqlite3

def create_orders_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create the orders table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            OR_ID INTEGER,
            User_Name TEXT,
            Operator_Name TEXT,
            Order_Cost INTEGER,
            Starting_Date TEXT,
            Ending_Date TEXT,
            User_Score INTEGER
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def add_order(user_name, operator_name, order_cost, starting_date, ending_date, user_score):
    create_orders_table()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''SELECT MAX(ID) FROM orders''')
    result = c.fetchone()
    next_id = 1 if result[0] is None else result[0] + 1

    c.execute('''
        INSERT INTO orders (ID, OR_ID, User_Name, Operator_Name, Order_Cost, Starting_Date, Ending_Date, User_Score)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (next_id, None, user_name, operator_name, order_cost, starting_date, ending_date, user_score))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

