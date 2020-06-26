#from smbus2 import SMBus

#import os
import sys
import time
from bme280 import BME280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)

bme280 = BME280(i2c_dev=bus)

try:
    while True:
        print(bme280.get_temperature())
        print(bme280.get_pressure(), bme280.get_humidity())
        time.sleep(1.0)

except KeyboardInterrupt:
    sys.exit(0)
