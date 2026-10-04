import pygame
import socket
import time

def getc():
    try:
        global c
        (c, cadd) = s.accept()
        print("Got client")
        return c
    except:
        print("errror")

def send(z):
    global c
    try:
        c.send(z.encode())
    except:
        print("errror waiting for new conn")
        (c, cadd) = s.accept()


def n20(x, y):
    global lastc
    pos = "None"
    cmd = "s"
    if (y <= -0.5 and x <= -0.5):
        pos = "top left"
        #cmd = "q"
    elif (y <= -0.5 and x < 0.5 and x > -0.5):
        pos = "TOp middle"
        cmd = "w"
    elif (y <= -0.5 and x >= 0.5):
        pos = "TOp right"
        #cmd = "e"
    elif (y > -0.5 and y < 0.5 and x <= -0.5):
        pos = "middle left"
        cmd = "a"
    elif (y > -0.5 and y < 0.5 and x < 0.5 and x > -0.5):
        pos = "middle middle"
        cmd = "s"
    elif (y > -0.5 and y < 0.5 and x >= 0.5):
        pos = "middle right"
        cmd = "d"
    elif (y >= 0.5 and x <= -0.5):
        pos = "bottom left"
        #cmd = "z"
    elif (y >= 0.5 and x < 0.5 and x > -0.5):
        pos = "bottom middle"
        cmd = "x"
    elif (y >= 0.5 and x >= 0.5):
        pos = "bottom right"
        #cmd = "c"
    if cmd == lastc:
        0
    else:
        #print(cmd)
        lastc = cmd
        return cmd


def servo(x, y):
    global lastc
    pos = "None"
    cmd = None
    if (y <= -0.5 and x <= -0.5):
        pos = "top left"
        cmd = "p"
    elif (y <= -0.5 and x < 0.5 and x > -0.5):
        pos = "TOp middle"
        cmd = "u"
    elif (y <= -0.5 and x >= 0.5):
        pos = "TOp right"
        cmd = "d"
    elif (y >= 0.5 and x <= -0.5):
        pos = "bottom left"
        cmd = "l"
    elif (y >= 0.5 and x < 0.5 and x > -0.5):
        pos = "bottom middle"
        cmd = "b"
    elif (y >= 0.5 and x >= 0.5):
        pos = "bottom right"
        cmd = "r"
    if cmd == lastc:
        return None
    else:
        #print(cmd)
        return cmd


pygame.init()
pygame.joystick.init()
print(pygame.joystick.get_count())
joystick1 = pygame.joystick.Joystick(0)
joystick1.init()
print(joystick1.get_numaxes())
#joystick2 = pygame.joystick.Joystick()
#joystick2.init()
#print(joystick2.get_numaxes())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4433))
s.listen(5)
print("Initializing Server. Waiting for Client.")
c = getc()

global lastc
lastc = "None"
while (1):
    pygame.event.get()
    x1 = round(joystick1.get_axis(0), 1)
    y1 = round(joystick1.get_axis(1), 1)
    x2 = round(joystick1.get_axis(2), 1)
    y2 = round(joystick1.get_axis(3), 1)
    #print(str(x1) + "  " + str(y1))
    cmd1 = n20(x1, y1)
    cmd2 = servo(x2, y2)
    if cmd1 == None:
        0
    elif cmd1 == "s":
        print("s" + "sp")
        send("s" + "sp")
    else:
        print(cmd1 + "st")
        send(cmd1 + "st")
    if cmd2 == None:
        0
    else:
        print(cmd2 + "sr")
        time.sleep(0.4)
        send(cmd2 + "sr")

