# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine, network, time
#os.dupterm(None, 1) # disable REPL on UART(0)
station = network.WLAN(network.STA_IF)
station.active(True)
#station.connect('OPPO A15s', 'senthil_43')
#station.connect('ASTRO', '12345678')
station.connect('JAI_TP-Link-2.4G', 'ganesh31114')
loopido = 0
while(not station.isconnected() and loopido <= 40):
    time.sleep_ms(50)
    loopido += 1
if(station.isconnected()):
    print("Connected to " + str(station.config("essid")))
else:
    print("Unable to connect!")

import gc
#import webrepl
#webrepl.start()
gc.collect()
