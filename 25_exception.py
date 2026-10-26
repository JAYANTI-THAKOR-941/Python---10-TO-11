# Exception handling

# try:
#     number = int(input("Enter any number:"))
#     print("Square:",number*number)
# except ValueError:
#     print("Please enter valid number.")

# try:
#     number1 = int(input("Enter any number:"))
#     number2 = int(input("Enter any number:"))
#     x = number1 / number2
#     print("Ans:",x)
# except ZeroDivisionError:
#     print("Can not devide by zero.")
 

try:
    number1 = int(input("Enter any number:"))
    number2 = int(input("Enter any number:"))
    x = number1 / number2
    print("Ans:",x)
except ZeroDivisionError:
    print("Can not devide by zero.")
except ValueError:
    print("Please enter valid value.")