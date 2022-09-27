import usocket
import ussl
import json
import WifiConnection

WifiConnection.connect()

def getHttpsUrl(domain, query):
    s = usocket.socket()
    ai = usocket.getaddrinfo(domain, 443)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ussl.wrap_socket(s, server_hostname=domain)
    print(s)

    s.write(b"GET "+query+" HTTP/1.0\r\nHost: "+domain+"\r\nUser-Agent: My raspberry pi pico tests\r\nAccept: application/json\r\n\r\n")
    while True:
        a = s.readline()
        if not a or a == b"\r\n":
            break
    obj = json.load(s)
    s.close()
    return obj

print(getHttpsUrl('dummyjson.com', '/products/1'))