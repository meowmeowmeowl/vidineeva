import RPi.GPIO as rp
import time
leds = [2,3,4,17,27,22,10,9]

rp.setmode(rp.BCM)
rp.setup(leds, rp.OUT)
for i2 in range(3):
    for i in range(8):
        rp.output(leds[i], 1)
        time.sleep(0.2)
        rp.output(leds[i], 0)
rp.cleanup()