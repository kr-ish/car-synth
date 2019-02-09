from gpiozero import PWMLED, Button
from signal import pause
from time import sleep
import time

import csv

speed = []
rpm = []
throttle = []
with open("obd-log-1549736212.1.csv","r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(row)
        #print(' '.join(row))
        if (row[1] == ' SPEED'):
            speed.append(row[2].split()[0])
        if (row[1] == ' RPM'):
            rpm.append(row[2].split()[0])
        if (row[1] == ' THROTTLE_POS'):
            throttle.append(row[2].split()[0])

led1 = PWMLED(17, frequency=490)
led2 = PWMLED(18, frequency=490)
led3 = PWMLED(22, frequency=490)
led4 = PWMLED(23, frequency=490)

initial = time.time()
counter = 0

while (time.time() - initial < 20):
    timeref = time.time()
    timestep = .5
    if ((time.time() - timeref) < timestep): 
        led1.value = float(speed[counter]) / 50.0
        led2.value = (float(rpm[counter]) - 500.0) / 1500.0
        led3.value = (float(throttle[counter]) - 5.0) / 30.0
        led4.value = float(speed[counter]) / 50.0
        counter += 1
    if counter >= len(speed):
        counter = 0


# button = Button(3)

# button.when_pressed = led.on
# button.when_released = led.off

# pause()

# value = 0.0
# while True:
#     value += 0.05
#     value = value % 1.0
#     led.value = value
#     sleep(0.1)

