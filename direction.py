from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_imu_config(False, True, False)                    #Enables the Gyroscope
gyro_only = sense.get_gyroscope()

print("p={pitch}; r={roll}; y={yaw}".format(**gyro_only))   # Show the Gyroscopic orientation

sense.show_letter("H")                                      # Show "H"
sleep(2)                                                    # Wait for 2s
sense.clear()                                               # Clear the display
