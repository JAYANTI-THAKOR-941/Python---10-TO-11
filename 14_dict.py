
server = {
    "name":"LAB-SERVER 01",
    "ip":"192.168.1.4",
    "port":8000,
    "is_online":True
}

# print(server).....
# print(server["name"])
# print(server["os"]) #error

# print(server.get("os","Not available"))

# server["os"] = "RedHat Server"
# server["port"] = 8080

# server.pop("port")
# print(server.pop("port","Not available"))
# print(server)

# for key in server:
#     print(key)

# for value in server.values():
#     print(value)

# for key,value in server.items():
#     print(f"{key.upper()} : {value} ")


#set
# ports = {22, 80, 443, 80, 22}
# print(ports)

# ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]

# unique_ip = set(ips)

# print(unique_ip)

allowed = {22, 80, 443}
open_ports = {22, 80, 3389, 21}

# set operation

# print(allowed & open_ports)
# print(allowed | open_ports)
# print(open_ports - allowed)
# print(open_ports ^ allowed)

