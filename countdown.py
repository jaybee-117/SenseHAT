
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
R = [0,0,255]
for i in range(9,-1,-1):
    sense.show_letter( str(i), R )
    sleep(1)

sense.clear()
