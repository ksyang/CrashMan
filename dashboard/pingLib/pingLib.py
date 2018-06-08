import socket

def sendPing(ip, pingPort):
	HOST = ip
	PORT = pingPort
	
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST, PORT))
		s.sendall(b'ping')
		data = s.recv(1024)
		return data.decode("utf-8")
	except:
		return "fail"

	
