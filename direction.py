from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
#Gyroscope
sense.set_imu_config(False, True, False)                    #Enables the Gyroscope
gyro_only = sense.get_gyroscope()
print("g_p={pitch}; g_r={roll}; g_y={yaw}".format(**gyro_only))

#Accelerometer
sense.set_imu_config(False, False, True)                    #Enables the Accelerometer
accel_only = sense.get_accelerometer()
print("a_p: {pitch}, a_r: {roll}, a_y: {yaw}".format(**accel_only)) 

sense.show_letter("H")                                      # Show "H"
sleep(2)                                                    # Wait for 2s
sense.clear()                                               # Clear the display
