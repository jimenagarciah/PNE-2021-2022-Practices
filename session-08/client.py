import socket

SERVER_IP = "localhost"
SERVER_PORT = 8081

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_IP, SERVER_PORT))

msg = "Hello from the client!"
msg_bytes = str.encode(msg)
client_socket.send(msg_bytes)

msg_bytes = client_socket.recv(2048)
msg = msg_bytes.decode("utf-8")
print(f"Message from server: {msg}")

client_socket.close()
