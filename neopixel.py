import Leds
import utime

l = Leds.Leds()

colors = [
    (2,0,0),
    (1,1,0),
    (0,2,0),
    (0,1,1),
    (0,0,2),
    (1,0,1),
    (0,0,0),
]

for j in range(0,l.max+6):
    for i, c in enumerate(colors):
        l.setLed(j-i, c)
    l.write()
    utime.sleep(0.15)

l.off()
