import socket
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("0.0.0.0", 9090))
s.listen(40)
print("listening on 9090")
while True:
	conn,addr=s.accept()
	print(f" Got Connection from {addr}")
	conn.sendall(b"hello!")
	conn.close()
