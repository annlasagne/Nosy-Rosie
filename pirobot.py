# A program to control the movement of a single motor using the RTK MCB!
# Composed by The Raspberry Pi Guy to accompany his tutorial!

# Let's import the modules we will need!
from time import sleep
import RPi.GPIO as GPIO

# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

print('Starting motor sequence')

# forwards
GPIO.output(17, 1)
GPIO.output(23, 1)
sleep(1)
GPIO.output(17,0)
GPIO.output(23,0)
sleep(1)
# turn left                          
GPIO.output(23, 1)
sleep(0.8)
GPIO.output(23,0)

# forwards    
# GPIO.output(17, 1)
# GPIO.output(23, 1)
# sleep(1)
# GPIO.output(17,0)
# GPIO.output(23,0)

#left
# GPIO.output(18,0.2)
# sleep(1)

# forward
# GPIO.output(17,1)
# GPIO.output(23,1)
# sleep(1)

# back
# GPIO.output(18,1)
# GPIO.output(22,1)
# sleep(1)

#turn right
# GPIO.output(18,1)
# sleep(1)

print('Finishing up!')
GPIO.cleanup()
