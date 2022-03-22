import socket

SERVER_IP = "localhost"
SERVER_PORT = 8081

while True:
    # -- Ask the user for the message
    msg = input(">> ")
    # -- Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- Establish the connection to the Server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    # -- Send the user message
    msg_bytes = str.encode(msg)
    client_socket.send(msg_bytes)
    # -- Close the socket
    client_socket.close()
