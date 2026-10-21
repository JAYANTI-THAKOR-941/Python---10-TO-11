# file handling in python

# with open("pythonData.txt","w",encoding="utf-8") as f:
#     f.write("Import Coffee, Export Code.")
#     f.write("\nThink before you click")

# with open("pythonData.txt","a",encoding="utf-8") as f:
#     f.write("\nSee something wrong? Do something right.")

# with open("pythonData.txt","a",encoding="utf-8") as f:
#     f.write("\nSecure your cyberspace, secure your digital life")

course = "Python Programming"
duration = 3.5

with open("pythonData.txt","a",encoding="utf-8") as f:
    f.write(f"\n{course} duration is {duration} Months.")

# read file
# f = open("cyber.txt","r",encoding="utf-8")
# lines = f.read()
# f.close()
# print(lines)