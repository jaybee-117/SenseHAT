from sense_hat import *
from time import sleep

sense = SenseHat()

while True:
    sleep (1)
    myfile = open("Temp.txt", "a")
    myfile.write(str(sense.temp))
    myfile.write("\n")
    myfile.close()

