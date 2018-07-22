import RPi.GPIO as gpio
import time
import smtplib

gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.IN)
username='aakashkolekar98@gmail.com'
password='washingma'

sender='aakashkolekar98@gmail.com'
recepient='aakashkolekar98@gmail.com'


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
            
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()#used to identify the computer
            mail.starttls()#tls-transport layer security
            mail.login('aakashkolekar98','washingma')
            
            header="To: "+recepient+"\n"+"From: "+username+"\n"+"Subject: SMTP Email test"
            content='BOSS \n Intruder detected'
            content=header+"\n"+content

            mail.sendmail('aakashkolekar98@gmail.com','aakashkolekar98@gmail.com',content)
            
            mail.close()
            
            time.sleep(5)
            time.sleep(0.1)
except:
    gpio.cleanup()
    



