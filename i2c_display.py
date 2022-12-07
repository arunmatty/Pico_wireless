from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import max30100

mx30 = max30100.MAX30100()
mx30.ir, mx30.red = mx30.read_sensor()

ms30.enable_spo2()
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("AK's Innovations", 0, 0)
oled.show()