from machine import Pin
import neopixel

class Leds:
    def __init__(self):
        self.max = 43

        pin = Pin(1, Pin.OUT)
        self.np = neopixel.NeoPixel(pin, self.max)
        self.off()

    def off(self):
        self.np.fill((0,0,0))
        self.np.write()

    def setLed(self, i, color):
        if i < self.max and i >= 0:
            self.np[i] = color
            
    def write(self):
        self.np.write()

