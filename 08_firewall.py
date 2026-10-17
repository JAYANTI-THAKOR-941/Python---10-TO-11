
ip = input("Enter source ip:")
port = input("Enter destination port:")

allowed_port = ["80","443","22"]
blocked_ip = ["192.168.1.50","192.168.1.41","192.168.1.22"]

if ip in blocked_ip:
    print("Deny:Your ip is blocked.")
elif not port in allowed_port:
    print("Deny:This port is not allowed.")
elif not ip.startswith("192.168."):
    print("Deny:Only c class ip allowed.!")
else:
    print("Allowed.")