# loop in python

correctPassword = "ved12345"

passwordList = [
    "ved123",
    "ved@123",
    "1234",
    "123",
    "Ved#221",
    "12345678",
    "ved12345",
    "student@123",
    "admin",
    "admin@123"
]

for password in passwordList:
    if password == correctPassword:
        print("Correct Password:",password)
        break
    else:
        print("Password does not match.!")