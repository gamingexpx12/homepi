# Made in gamingexpx12, not china.

from grovepi import *
from grove_rgb_lcd import *
import time

# Pref
dhtsensor = 7 # DI pin with PWM
# display is ic2 based

pinMode(dhtsensor, "input")
out = ""
prevt = 0
prevhum = 0
# Main
time.sleep(1)
while True:
    try:
        t, hum = dht(dhtsensor, 0)
        out = "It's {:2}C degrees and {:3.0f} percent humidity".format(t,hum)
        time.sleep(0.1)
        if t == prevt and hum == prevhum:
            print("No changes: {} {}, {} {} ".format(t,prevt,hum,prevhum))
            pass
        else:
            setText(out)
            setRGB(0,128,64)
            print(out)
        prevt = t
        prevhum = hum
        time.sleep(2)
    except KeyboardInterrupt:
        break
        setText("")
        setRGB(0,0,0)
    except IOError:
        print "Error"
