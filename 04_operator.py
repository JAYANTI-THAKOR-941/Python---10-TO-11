# Login
correctUsername = "jayanti@123"
correctPassword = "123@pipl"
correctPIN = "121233"

username = input("Enter your username:")
password = input("Enter your password:")

if username == correctUsername and password == correctPassword:
    SECURITY_PIN = input("Enter PIN:")
    if SECURITY_PIN == correctPIN:
        print("Login successfully.!")
    else:
        print("Incorrect PIN.")
else:
    print("ERROR:invalid username and password.!")



