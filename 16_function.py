




# function in python

# definition
# def greetStudent():
#     print("Hello Student.!")

# # function calling
# greetStudent()
# greetStudent()

# def greetUser(name = "User"):
#     print(f"Hello,{name}")

# greetUser("Ved")
# greetUser("Jignesh")
# greetUser()


# def calc(n1,n2):
#    return n1+n2

# print("Addition:",calc(10,50))

def calc(*nums):
   return sum(nums)

print("Addition:",calc(10,50,50,22,545))
print("Addition:",calc(10,50,50,22,545,333,3,43,54))