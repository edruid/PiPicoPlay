from machine import Pin
import utime

class Ultra:
    def __init__(self):
        self.echo = Pin(0, Pin.IN)
        self.trig = Pin(2, Pin.OUT)
        self.trig.low()
        utime.sleep_us(2)

    def sense(self):
        self.trig.high()
        utime.sleep_us(5)
        self.trig.low()
        while self.echo.value() == 0:
            start = utime.ticks_us()
        while self.echo.value() == 1:
            stop = utime.ticks_us()
        return (stop - start) * 0.0343 / 2