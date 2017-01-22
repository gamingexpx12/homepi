# Made in gamingexpx12, not china.

from grovepi import *
import time

# Pref
dhtsensor = 7 # DI pin with PWM

pinMode(dhtsensor, "input")
out = ""
# Main
time.sleep(1)
while True:
    try:
        t, hum = dht(dhtsensor)
        out = "It's {}*C degrees and {} percent humidity".format(t,hum)
        print(out)
        time.sleep(1)
    except KeyboardInterrupt:
        break
    except IOError:
        print "Error"
