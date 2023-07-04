import add_users
import add_operators
import add_orders
import check_password
import requests
import user
import operatorr

import tkinter as tk


def start_program():
    # Close the window
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Welcome Page")
window.geometry("900x700")  # Set the window size to 600x500 pixels

# Create a frame to hold the image
image_frame = tk.Frame(window)
image_frame.pack(pady=20)

# Load and display the image
image = tk.PhotoImage(file="sanati_hamedan_resized.png")
image_label = tk.Label(image_frame, image=image)
image_label.pack()

# Create a frame to hold the labels and button
content_frame = tk.Frame(window)
content_frame.pack(pady=50)

# Create a label to display the first designer's name
label1 = tk.Label(content_frame, text="Program Designed By Majid ", font=("Arial", 20, "bold"))
label1.pack(pady=10)


# Create a frame to hold the button
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Create a "Start" button
start_button = tk.Button(button_frame, text="Start", command=start_program, font=("Arial", 16, "bold"))
start_button.pack(ipadx=10, ipady=5)

# Run the event loop
window.mainloop()




print("----------------------------------------------")
print("Hi,Welcome to Remote work service :)")
print("----------------------------------------------")

option = 0
#main loop
while True:
    print("----------------------------------------------")
    print("select one of the options")
    print("1: add a user")
    print("2: add an operator")
    print("3: log in as a user")
    print("4: log in as an operator")
    print("5: see orders")
    print("10: exit")
    print("----------------------------------------------")
    while True:
        option = int(input("enter your choice:   "))
        if 0 < option < 6 or option == 10:
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
        operatorr.operator_login()
    elif option == 5:
        requests.see_orders()
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
