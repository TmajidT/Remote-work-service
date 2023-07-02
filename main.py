import add_users
import add_operators
import add_orders
import check_password
import requests
import user
import operator

print("----------------------------------------------")
print("Hi,Welcome to Remote work service :)")
print("----------------------------------------------")

option = 0
while True:
    print("----------------------------------------------")
    print("select one of the options")
    print("1: add a user")
    print("2: add an operator")
    print("3: log in as a user")
    print("4: log in as an operator")
    print("10: exit")
    print("----------------------------------------------")
    while True:
        option = input("enter your choice:   ")
        if 0 < option < 5 or option == 10:
            break
        else:
            print("please enter a valid number")
            print("----------------------------------------------")

    if option == 1:
        add_users.add_user()
    elif option == 2:
        add_operators.add_operator()
    elif option == 3:
        user.user_login()
    elif option == 4:
        operator.operator_login()
    elif option == 10:
        break







# all of the abilities ---- you can delete # and use them
# --------------------------------------------------------------------

# add a user
# add_users.add_user()


# add an operator
# add_operators.add_operator()


# add an order
# add_orders.add_order("johnsmith", "operator1", 50, "2023-07-01", "2023-07-05", 25)


# check if the password is currect
# print(check_password.check_user_password("majid"))
# print(check_password.check_operator_password("majid"))


# create a job request by user
# requests.add_job_request("johnsmith", "I need help with website developmentqeporjoaepgjoaepofgjadpofj;", 200, "2023-07-10")


# show all the requests
# requests.show_all_job_requests()
