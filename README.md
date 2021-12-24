# SenseHAT
Experimentation with the SenseHAT

## Calibration
![Orientation Axes](/Orientation.png "Orientation Axes")
For calibrating the SenseHAT IMU, first install octave:
```bash
sudo apt install octave -y
```
Copy the following files to a temporary folder:
```bash
cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
```
Run the calibration tool:
```bash
cd RTEllipsoidFit
RTIMULibCal
```
Following that, select what you want to calibrate and then to stop the calibration with 's' and then 'x'
