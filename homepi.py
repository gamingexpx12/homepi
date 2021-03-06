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
        out = "Det er {:2.0f} grader inne".format(t)
        time.sleep(0.1)
        if t == prevt:
            print("No changes: {} {}".format(t,prevt))
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
