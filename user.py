import check_password
import requests

def user_login():
    print("user login section!")
    option = 0


    user_name = input("pleas enter your user name: ")
    if check_password.check_user_password(user_name) is False:
        print("pleas try again!")
    else:
        print("----------------------------------------------")
        print("1: add a job request")
        print("10: exit")
        while True:
            option = input("enter your choice:   ")
            if 0 < option < 2 or option == 10:
                break
            else:
                print("please enter a valid number")
                print("----------------------------------------------")
        if option == 1:
            user_request = input("please enter your job request: ")
            order_cost = 0
            order_cost = input("how much are you willing to pay?  ")
            #shold add ending_date
            requests.add_job_request(user_name,user_request,order_cost,)

        elif option == 10:
            print("exiting user section")

