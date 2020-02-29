import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET =IPV address from the internet with a pair of host & port nr.(host is url or address ,port is integer)
# SOCK_STREAM= TCP protocol

print("Socket successfully created")

soc.bind((socket.gethostname(), 1024))
print("socket binded to port:", (1024))

soc.listen(5)
print("socket is listening")

while True:  # while the connection is true accept the client address and socket
    client, address=soc.accept()
    print(f"Connected to the {address} ")
    client.send(bytes("Thank you for connecting", " UTF-8"))


