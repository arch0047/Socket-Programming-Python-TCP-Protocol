
import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.connect((socket.gethostname(), 1024))
print("Socket is successfully created")

message = soc.recv(1024)  # byte as a parameter
print(message.decode("UTF-8 "))  # as the sent message was incoaded so decoding it now

soc.close()




