# if else statement in python

ip = input("Enter source ip:")
port = input("Enter destination port:")

blocked_ip = ["10.0.0.5","10.1.1.6","203.1.1.10","203.1.1.6"]
allowed_port = ["80","443","22"]

if ip in blocked_ip:
    print("DENY:This IP is Blocked.!")
elif not port in allowed_port:
    print("DENY:This port is not allowed.!")
elif not ip.startswith("192.168."):
    print("DENY:Only Class C IP Allowed.")
else:
    print("Allow.!")