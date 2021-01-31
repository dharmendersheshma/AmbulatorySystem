import socket
import json
import netifaces

gateways = netifaces.gateways()
default_gateway = gateways['default'][netifaces.AF_INET][0]
print(default_gateway)

HOST = "localhost"
PORT = 5050
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('Socket created')
#
# try:
#     s.bind((HOST, PORT))
# except socket.error as err:
#     print('Bind failed. Error Code : ' .format(err))
# # s.listen(10)
# print("Socket Listening")
# conn, addr = s.accept()
# conn.send(bytes("Message"+"\r\n",'UTF-8'))
# print("Message sent")
# # while(True):
# #     conn.send(bytes("Message"+"\r\n",'UTF-8'))
# #     print("Message sent")
#     # data = conn.recv(1024)
#     # print(data.decode(encoding='UTF-8'))

arr = [1, 2, 3, 4, 5, 6.5, 7.369]
data = json.dumps({"PatientData":arr})

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# sock.sendall(data.encode())
# sock.sendall("\n".encode())
while True:
	print('Enter patient data:')
	for i in range(7):
		arr[i] = input()
	data = json.dumps({"PatientData":arr})
	sock.sendall(data.encode())
	sock.sendall("\n".encode())