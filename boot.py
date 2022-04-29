"""
Subrata Sarker <picklumithu@yahoo.com>
Date: 26.04.2022
Inspired from => https://RandomNerdTutorials.com
"""
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import esp
import credentials as creds


esp.osdebug(None)

import gc
gc.collect()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(creds.ssid, creds.password)

while not station.isconnected():
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(4, Pin.OUT)

with open("template.html") as f:
  html = f.read()
html = html or "The html file was not found!"