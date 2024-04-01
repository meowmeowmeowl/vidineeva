import RPi.GPIO as gpio
import time
def per(x):
    return [int(bit) for bit in bin(x)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

               
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT,initial = 0)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def adc():
    for i in range(256):
        d = per(i)
        gpio.output(dac, d)
        time.sleep(0.07)
        c = gpio.input(comp)
        if c == 1:
            return i
            break
    return 256
        
try:
    while True:
        x = adc()
        print(x, 3.3 * x / 256)
            
finally:
    gpio.output(dac, 0)
    gpio.cleanup()  