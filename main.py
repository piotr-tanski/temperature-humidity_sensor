from machine import Pin, I2C
from dht import DHT11, InvalidChecksum, InvalidPulseCount
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import utime as time


pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)


I2C_ADDR     = const(0x27)
I2C_NUM_ROWS = const(2)
I2C_NUM_COLS = const(16)
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


def updateDisplay(temperature, humidity):
    lcd.clear() # Clear text displayed previously
    lcd.putstr("{} C".format(temperature))
    lcd.move_to(0, 1) # Move to second row
    lcd.putstr("{} %".format(humidity))


while True:
    time.sleep(5)
    try:
        updateDisplay(sensor.temperature, sensor.humidity)
    except InvalidChecksum as e:
        print("{}. Continue...", e)
    except InvalidPulseCount as e:
        print("{}. Continue...", e)