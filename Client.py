import socket
import base64

UDP_IP = "10.160.108.101"
UDP_PORT = 5005

MESSAGE= "cinema"



sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print ("received message:", data)

idx=0
test=0
tab=[]
for idx in range (4):
    tab.append(data[idx])
    
test= data[3]<<24 | data[2]<<16 | data[1]<<8

print(tab)
print(test)

test=str(test)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)

