
password = input("Enter password:")

print("Length:",len(password))
if not(len(password)>= 8 and len(password) <=64):
    print("Your password is week or too long")
else:
    print("Your password is strong.!")