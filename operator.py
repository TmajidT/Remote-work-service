import sqlite3
import check_password
import requests
import add_orders


def operator_login():
    print("operator login section!")
    option = 0

    operator_user_name = input("pleas enter your user name: ")
    if check_password.check_operator_password(operator_user_name) is False:
        print("pleas try again!")
    else:
        print("----------------------------------------------")
        print("1: accept a job request")
        print("10: exit")
        while True:
            option = input("enter your choice:   ")
            if 0 < option < 2 or option == 10:
                break
            else:
                print("please enter a valid number")
                print("----------------------------------------------")
        if option == 1:
            row_number = requests.show_all_job_requests()
            while True:
                accepted_job = input("witch job do you want to accept:  ")
                if 0 < accepted_job <= row_number:
                    break
                else:
                    print("enter a valid number!")


            #get users data
            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            c.execute('SELECT * FROM job_requests WHERE ID = ?', (accepted_job,))
            result = c.fetchone()
            conn.close()


            #to get operators score
            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            c.execute('SELECT * FROM operator WHERE User_Name = ?', (operator_user_name,))
            operator_result = c.fetchone()
            conn.close()



            add_orders.add_order(result[1],operator_user_name,result[3],result[4],result[5],operator_result[8])







        elif option == 10:
            print("exiting user section")

