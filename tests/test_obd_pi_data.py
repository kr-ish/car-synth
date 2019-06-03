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

# while (time.time() - initial < 20):
while (True):
    # timeref = time.time()
    timestep = 1.0
    # if ((time.time() - timeref) < timestep):

    
    val =  float(speed[counter]) / 150.0
    if val > 1.0:
        val = 1.0
    elif val < 0.0:
        val = 0.0
    print val
    led1.value = val

    
    val = (float(rpm[counter]) - 500) / 1500
    if val > 1.0:
        val = 1.0
    elif val < 0.0:
        val = 0.0
    print val
    led2.value = val

    
    val = (float(throttle[counter]) - 5.0) / 30.0
    if val > 1.0:
        val = 1.0
    elif val < 0.0:
        val = 0.0
    print val
    led3.value = val
    
    val = float(speed[counter]) / 150.0
    if val > 1.0:
        val = 1.0
    elif val < 0.0:
        val = 0.0
    print val
    led4.value = val

    counter += 1

    if counter >= len(speed):
        counter = 0

    time.sleep(timestep)


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

