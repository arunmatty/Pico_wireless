from machine import Pin
import utime 

led = machine.Pin(0, machine.Pin.OUT)

while True:
    led.value(0)
    utime.sleep(1)
    led.value(1)
    utime.sleep(1)
    
