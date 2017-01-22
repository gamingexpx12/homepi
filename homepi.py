# Made in gamingexpx12, not china.

from grovepi import *
from grove_rgb_lcd import *
import time

# Pref
dhtsensor = 7 # DI pin with PWM
# display is ic2 based

pinMode(dhtsensor, "input")
out = ""
# Main
time.sleep(1)
while True:
    try:
        t, hum = dht(dhtsensor, 0)
        out = "It's {}*C degrees and {} percent humidity".format(t,hum)
        time.sleep(0.1)
        setText(out)
        setRGB(0,128,64)
        print(out)
        time.sleep(1)
    except KeyboardInterrupt:
        break
        setText("")
        setRGB(0,0,0)
    except IOError:
        print "Error"
