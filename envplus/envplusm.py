#!/usr/bin/python3
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from enviroplus import gas
from bme280 import BME280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)

class Envrioplus:
  def __init__(self):
    self.bme_280 = BME280(i2c_dev=bus)

  def get_temperature(self):
    return self.bme_280.get_temperature()
  def get_pressure(self):
    return self.bme_280.get_pressure()
  def get_humidity(self):
    return self.bme_280.get_humidity()

  def get_proximity(self):
      return ltr559.get_proximity()
  def get_lux(self):
      return ltr559.get_lux()

  def get_oxidising(self):
      data = gas.read_all()
      return data.oxidising / 1000
  def get_reducing(self):
      data = gas.read_all()
      return data.reducing / 1000
  def get_nh3(self):
      data = gas.read_all()
      return data.nh3 / 1000
