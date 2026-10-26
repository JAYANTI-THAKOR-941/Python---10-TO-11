import socket

HOST = "0.0.0.0"    
PORT = 5000


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server IP: {get_local_ip()}   Port: {PORT}")
    print("Waiting for a client...")

    conn, addr = server.accept()
    with conn:
        print(f"Connected: {addr[0]}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client disconnected.")
                break
            message = data.decode(errors="replace")
            print("Client:", message)
            if message.lower() == "quit":
                break
            reply = input("You: ")
            conn.sendall(reply.encode())
            if reply.lower() == "quit":
                break
print("Server closed.")