from machine import Pin
import HcSr04
import Leds
import utime

ultra = HcSr04.Ultra()
leds = Leds.Leds()

while 1:
    dist = ultra.sense()
    print(dist, 'cm')
    leds.setLed(int(dist / 2), (0,0,1))
    leds.write()
    utime.sleep(0.5)
    leds.setLed(int(dist / 2), (0,0,0))
    