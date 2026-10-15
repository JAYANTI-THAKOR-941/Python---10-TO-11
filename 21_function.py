
def addition(n1,n2):
    return n1+n2

print("Addition:",addition(50,20))

def addition(*nums):
    return sum(nums)

print("Addition:",addition(50,20,5,40,90))
print("Addition:",addition(50,20))
print("Addition:",addition(50,20,80))