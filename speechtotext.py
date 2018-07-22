import speech_recognition as sr
import socket
import webbrowser as wb
from texttospeech import *
chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

client=socket.socket()
client.connect(("172.20.10.9",1233))
#send=input()
#client.sendall(send.encode())

r=sr.Recognizer()
print('What Can I Do For You?')
while True:
    with sr.Microphone() as source:
        audio=r.listen(source)

    try:
        #print("I think you just said:\n"+r.recognize_google(audio))
        send=(r.recognize_google(audio))
        print(send)
        send1=send.encode()
        client.sendall(send1)
        if send == 'lights on':
            wb.get(chrome_path).open('''https://maker.ifttt.com/trigger/Lights On/with/key/IOS179sAMv3bvre01fvXSgRGFarSdg3OidY29RmGQS''')
            tts('Lights have been turned on','en')
            #print("hi")
        elif send == 'lights off':
            wb.get(chrome_path).open('''https://maker.ifttt.com/trigger/Lights Off/with/key/IOS179sAMv3bvre01fvXSgRGFarSdg3OidY29RmGQS''')
            tts('Lights have been turned off','en')
            #print("hi")
        print('Boss do you have anything else?')
        tts('Boss do you have anything else','en')
        

    except Exception as e:
        print(e)
