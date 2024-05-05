from machine import Pin
from servo import Servo
import time, socket, sys

def moton(char):
    print(char)
    if(char == "q"):
        m1a.on()
        m1b.off()
    elif(char == "z"):
        m1a.off()
        m1b.on()
    elif(char == "e"):
        m2a.on()
        m2b.off()
    elif(char == "c"):
        m2a.off()
        m2b.on()
    elif(char == "w"):
        m1a.on()
        m1b.off()
        m2a.on()
        m2b.off()
    elif(char == "x"):
        m1a.off()
        m1b.on()
        m2a.off()
        m2b.on()
    elif(char == "a"):
        m1a.off()
        m1b.on()
        m2a.on()
        m2b.off()
    elif(char == "d"):
        m1a.on()
        m1b.off()
        m2a.off()
        m2b.on()
    elif(char == "s"):
        m1a.on()
        m1b.off()
        m2a.on()
        m2b.off()

def motoff(char):
    if(char == "q" or char == "z"):
        m1a.off()
        m1b.off()
    elif(char == "e" or char == "c"):
        m2a.off()
        m2b.off()
    elif(char in ['w', 'a', 's', 'd', 'x']):
        m1a.off()
        m1b.off()
        m2a.off()
        m2b.off()

def serve(char):
    global serv1
    global serv2
    if(char == 'p' and serv1 <= 170 ):
        serv1 += 10
        servo1.move(serv1)
    elif(char == 'l' and serv1 >= 10):
        serv1 -= 10
        servo1.move(serv1)
    elif(char == 'd' and serv2 <= 170 ):
        serv2 += 10
        servo2.move(serv2)
    elif(char == 'r' and serv2 >= 10):
        serv2 -= 10
        servo2.move(serv2)
    elif(char == 'u'):
        if(serv2 <= 170):
            serv2 += 10
            servo2.move(serv2)
        if(serv1 <= 170):
            serv1 += 10
            servo1.move(serv1)
    elif(char == 'b'):
        if(serv1 >= 10):
            serv1 -= 10
            servo1.move(serv1)
        if(serv2 >= 10):
            serv2 -= 10
            servo2.move(serv2)
    elif(char == '='):
        diff = serv1 - serv2
        if(diff < 1):
            diff = diff * (-1)
        if(serv1 < serv2):
            serv1 += diff
            servo1.move(serv1)
        if(serv2 < serv1):
            serv2 += diff
            servo2.move(serv2)
    print(str(serv1) + ' ' + str(serv2))

global serv1
serv1 = 0
global serv2
serv2 = 0
led = Pin(2, Pin.OUT)
m1a = Pin(16, Pin.OUT)
m1b = Pin(14, Pin.OUT)
m2a = Pin(12, Pin.OUT)
m2b = Pin(13, Pin.OUT)
led.off()
m1a.off()
m1b.off()
m2a.off()
m2b.off()
global servo
servo1 = Servo(pin=5)
servo2 = Servo(pin=4)
s = socket.socket()
k = 0
while True:
    try:
        print("Socket Connect")
        s.close()
        s = socket.socket()
        s.connect(("192.168.1.7", 9999))
        break
    except Exception as error:
        print(error)
    time.sleep_ms(50)
    k += 1
    if(k > 5):
        sys.exit()
k = 0
while(True):
    while(True):
        try:
            r = s.recv(3).decode()
            break	
        except:
            print("Unable to get info")
            while k <= 5:
                try:
                    print("reconnect")
                    s.close()
                    s = socket.socket()
                    s.connect(("192.168.1.7", 9999))
                    break
                except Exception as error:
                    print(error)
                k += 1
                if(k > 5):
                    sys.exit()

    print(r)
    cmd = str(r[1:3])
    if(cmd == "st"):
        moton(r[0])
    elif(cmd == "sp"):
        motoff(r[0])
    elif(cmd == "sr"):
        serve(r[0])        
    