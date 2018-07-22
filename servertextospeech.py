import socket
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.OUT)

server=socket.socket()
server.bind(("172.20.10.9",1233))
server.listen(10)
conn,addr=server.accept()
while True:
    message=conn.recv(1000)
    #print(message.decode())
    msg=message.decode()
    
    if msg=='lights on':
        gpio.output(5,True)
        
    if msg=='lights off':
        gpio.output(5,False)
        
    #else:
        #conn.close()
        #server.close()
        #break