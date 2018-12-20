import socket
import base64

UDP_IP = "10.160.108.101"
UDP_PORT = 5005

MESSAGE= "cinema"

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))



while True:
        data, addr = sock.recvfrom(1024)
        print ("received message:", data)

     
