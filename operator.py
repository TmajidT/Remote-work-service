import check_password
import requests
import add_orders


def user_login():
    print("operator login section!")
    option = 0

    user_name = input("pleas enter your user name: ")
    if check_password.check_operator_password(user_name) is False:
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

            add_orders.add_order()







        elif option == 10:
            print("exiting user section")

