from client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
SERVER_IP = "localhost"
SERVER_PORT = 8081

# -- Create a client object
c = Client(SERVER_IP, SERVER_PORT)
print(c)