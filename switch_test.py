from gpiozero import Button
from time import sleep

# Setup GPIO
on_switch = Button(24, pull_up=True)  # connect to GND
mode_switch = Button(27, pull_up=True)  # connect to GND


# switch on
on_switch.wait_for_press()
print('on switch pressed')

# main
while (True):

    while(mode_switch.is_pressed):
        print('alg mode')
        sleep(0.1)
    while(not mode_switch.is_pressed):
        print('simple mode')
        sleep(0.1)
