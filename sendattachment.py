import RPi.GPIO as gpio
import time
import smtplib
import imghdr
from email.message import EmailMessage
from picamera import PiCamera

gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.IN)
username='aakashkolekar98@gmail.com'
password='washingma'

sender='aakashkolekar98@gmail.com'
recepient='aakashkolekar98@gmail.com'
subject='Intruder Alert!!'
camera=PiCamera()

try:

    while True:
        time.sleep(2)#to stabilize the sensor
        
        x=gpio.input(5)
        print(x)
        
        if x==0:
            print("No intuder")
            time.sleep(5)
            time.sleep(0.1)
           
        elif x==1:
            
            print("Intruder detected")
            # s.ehlo()#used to identify the computer
            #s.starttls()#tls-transport layer security
            #s.login('aakashkolekar98','washingma')
            msg=EmailMessage()
            msg['From']=username
            msg['To']=recepient
            msg['Subject']=subject
               
            time.sleep(5)
            camera.capture('/home/pi/iot_vacation/untitled.jpg')
               
            filepath='/home/pi/iot_vacation/untitled.jpg'
            fp=open(filepath,'rb')#used to read bytes from a file
            part=fp.read()#read the file
            fp.close()
               
            msg.add_attachment(part,maintype='image',subtype=imghdr.what(None,part))
            s=smtplib.SMTP('smtp.gmail.com',587)
                
            '''header="To: "+recepient+"\n"+"From: "+username+"\n"+"Subject: SMTP Email test"
            content='BOSS \n Intruder detected'
            content=header+"\n"+content'''
            
            
            s.starttls()#tls-transport layer security
            s.login('aakashkolekar98','washingma')
            s.sendmail('aakashkolekar98@gmail.com','aakashkolekar98@gmail.com',msg.as_string())
            s.quit()
            
            time.sleep(5)
            time.sleep(0.1)
except:
    gpio.cleanup()
    




