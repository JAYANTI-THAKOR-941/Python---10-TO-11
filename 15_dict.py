# dictionary and set

server = {
    "name":"LAB-SERVER 01",
    "port":8000,
    "ip":"192.168.1.10",
    "is_online":True
}

# print(server)
# print("IP ADDRESS:",server["ip"])
# # print("SERVER OS:",server["os"]) # error
# # print("SERVER OS:",server.get("os","Windows"))

# server["os"] = "RedHat Linux" 
# server["port"] = 8080

# server.update({"port":5000,"ip":"192.168.1.15"})
# print(server)


# # server.pop("port")
# print(server.pop("RAM","UNKnown"))
# print(server)


# for key in server:
#     print(key)

# for value in server.values():
#     print(value)

# for key,value in server.items():
#     print(f"{key.title()} : {value}")

# set
# ports = {22, 80, 443, 80, 22}
# # print(ports)

# ips = ["10.0.0.5", "10.0.0.7", "10.0.0.5", "10.0.0.9", "10.0.0.7"]

# unique_ips = set(ips)
# print(unique_ips)


# allowed = {22, 80, 443}
# open_ports = {22, 80, 3389, 21}

# print(allowed & open_ports)
# print(allowed | open_ports)
# print(allowed - open_ports)
# print(open_ports - allowed )

# print(open_ports ^ allowed)










































