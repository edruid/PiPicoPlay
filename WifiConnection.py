import network

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Druid_EXT","secret")
