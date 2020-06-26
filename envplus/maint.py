#!/usr/bin/python3
import sys
import time
from envplusm import Envrioplus as env

E = env()
time.sleep(1.0)
try:
    while True:
        print (E.get_temperature(),E.get_humidity(),E.get_pressure())
        print ("-")
        print (E.get_lux(), E.get_proximity())
        time.sleep(1.0)

except KeyboardInterrupt:
    sys.exit(0)
