
# loop in python

# tuple
ALLOWED_PORT = (80,443,22)

# list
open_ports = [80,8080,5000,22,21,443,3000,24]

# empty list
unexcepted = []
allowed_found = []

for port in open_ports:
    if port in ALLOWED_PORT:
        allowed_found.append(port)
    else:
        unexcepted.append(port)

print()
print("=" * 34)
print(" PORT POLICY AUDITOR")
print("=" * 34)

print(f"Total Open Ports:{len(open_ports)}")
print(f"Total Allowed Ports:{len(allowed_found)}")
print(f"Total Unexcepted Ports:{len(unexcepted)}")

print()

unexcepted.sort()

if unexcepted:
    print("Review this ports.")
    for i,port in enumerate(unexcepted,start=1):
        print(f"{i}.PORT:{port}")
else:
    print("All open ports are allowed ports.")
