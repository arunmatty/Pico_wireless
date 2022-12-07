from machine import Pin
import time

led = Pin(0, Pin.OUT)
switch = Pin(1, Pin.IN)

while True:
    if(switch.value == 1):
        led.value(1)
      else:
        led.value(0)
        