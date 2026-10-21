# file handling in python

# create and write data in file

# with open("data.txt","w",encoding="utf-8") as f:
#     f.write("Welcome to Python Programming.\n")
#     f.write("Hello Students.!")

# with open("data.txt","a",encoding="utf-8") as f:
#     f.write("\n#File Handling in Python.!")

host = "localhost"
port = 8000
with open("data.txt","a",encoding="utf-8") as f:
    f.write(f"\n{host} is connected with port = {port}")

# read data from file
f = open("data.txt","r")
data = f.read()
f.close()
print(data)