import socket

PORT = 5000
server_ip = input("Server IP: ").strip()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(5)
    try:
        s.connect((server_ip, PORT))
    except ConnectionRefusedError:
        print("Connection refused: is the server running?")
        raise SystemExit
    except OSError as e:
        print(f"Could not connect: {e}")
        raise SystemExit

    s.settimeout(None)       # reply ka intezaar lamba ho sakta hai
    print("Connected. Type 'quit' to exit.")
    while True:
        message = input("You: ").strip()
        if message == "":
            continue
        s.sendall(message.encode())
        if message.lower() == "quit":
            break
        data = s.recv(1024)
        if not data:
            print("Server closed the connection.")
            break
        reply = data.decode(errors="replace")
        print("Server:", reply)
        if reply.lower() == "quit":
            break
print("Disconnected.")