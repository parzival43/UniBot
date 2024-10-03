import socket
from pynput import keyboard
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


def on_press(key):
    global st
    global c
    global lastc
    try:
        if(key.char != lastc and key.char in n):
            send(str(key.char) + "st")
            print(str(key.char) + "st")
        lastc = key.char
        if (key.char == '='):
            send(str(key.char) + "sr")
            print(str(key.char) + "sr")

    except:
        print("works")
        if (key == keyboard.Key['page_up']):
            send("psr")
            print("psr")
        if (key == keyboard.Key['left']):
            send("lsr")
            print("lsr")
        if (key == keyboard.Key['page_down']):
            send("dsr")
            print("dsr")
        if (key == keyboard.Key['right']):
            send("rsr")
            print("rsr")
        if (key == keyboard.Key['up']):
            send("usr")
            print("usr")
        if (key == keyboard.Key['down']):
            send("bsr")
            print("bsr")


""""
    if (key == keyboard.Key['left'] or key == keyboard.Key['right']) :
        if(key == keyboard.Key['left']):
            if(not i > 170):
                i += 10
        if (key == keyboard.Key['right']):
            if (not i < 10):
                i -= 10
        f = str(i)
        print(f)
        size = len(str(i))
        if (size == 1):
            f = "00" + f
        if (size == 2):
            f =  "0" + f
        print("'" + f + "'")
        try:
            send(f)
        except:
            #global c
            c = getc()
    if(key == keyboard.Key["up"] or key == keyboard.Key["down"]):
        if (key == keyboard.Key["up"]):
            send("upp")
        if (key == keyboard.Key["down"]):
            send("dow")
    """
def on_release(key1):
    global lastc
    global c
    try:
        if(key1.char in n and key1.char != '='):
            send(str(key1.char) + "sp")
            print(str(key1.char) + "sp")
            lastc = None
    except:
        0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4433))
s.listen(5)
print("Initializing Server. Waiting for Client.")
c = getc()
lastc = ""
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    global i
    i = 0
    n = ['q', 'a', 'z', 'w', 's', 'x', 'e', 'd', 'c', '=']
    listener.join()


