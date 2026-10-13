#list and tuple in python

# tuple
ALLOWED_PORT = (22,80,443)

# list
open_ports = [80,443,8080,5000,22,3389,5500,21,24]

# empty list
unexcepted = []
found_allowed = []
print("=" * 34)
print(" PORT POLICY AUDITOR")
print("=" * 34)

for port in open_ports:
    if port in ALLOWED_PORT:
        found_allowed.append(port)
    else:
        unexcepted.append(port)

print()

unexcepted.sort()

print(f"Total Open Ports:{len(open_ports)}")
print(f"Total Allowed Ports:{len(found_allowed)}")
print(f"Total Unexcepted Ports:{len(unexcepted)}")

if unexcepted:
    print("\nReview this ports.")
    for i,port in enumerate(unexcepted,start=1):
        print(f"{i}.PORT:{port}")

