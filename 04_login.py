# login system using if else
correctUsername = "prakshal.com"
correctPassword = "123@pipl"
correctPIN = "121233"

username = input("Enter username:")
password = input("Enter password:")

if username == correctUsername and password == correctPassword:
    PIN = input("Enter PIN:")
    if PIN == correctPIN:
        print("Login successfully.!")
    else:
        print("Incorrect PIN.")
else:
    print("Incorrect username and password.")