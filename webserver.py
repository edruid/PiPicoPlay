import socket
import network

from machine import Pin
import neopixel
import utime

import WifiConnection
import Leds
import HcSr04

WifiConnection.connect()
leds = Leds.Leds()
ultra = HcSr04.Ultra()

def qs_parse(line):
    try:
        parts = str(line).split(' ')[1].split('?')
    except:
        print('Bad line:', line)
        return {}
    if len(parts) < 2:
        return {}
    params = {}
    splits = parts[1].split('&')
    for split in splits:
        key, value = split.split('=')
        params[key] = value
    return params

sta_if = network.WLAN(network.STA_IF)
print(sta_if.ifconfig()[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    cl_file = cl.makefile('rwb', 0)
    line = cl_file.readline()
    params = qs_parse(line)
    print(params)
    dist = ultra.sense()
    if 'led' in params:
        leds.off()
        ledId = int(params['led'])
        distId = int(dist+0.5)
        for i in range(min(ledId, distId), max(ledId, distId)):
            leds.setLed(i, (1,0,0))
        leds.write()
    
    while True:
        line = cl_file.readline()
        print(line)
        if not line or line == b'\r\n':
            break
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send('Distance ' + str(dist) + ' cm')
    cl.send('set light <form><input type="number" name="led"/><input type="submit"/></form>')
    cl.close()