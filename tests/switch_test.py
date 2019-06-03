"""Quick test that the switches are working / wired correctly and the switch logic is working as intended."""

from gpiozero import Button
from time import sleep

# Setup GPIO
on_switch = Button(24, pull_up=True)  # connect to GND
mode_switch = Button(27, pull_up=True)  # connect to GND

# main
while True:

    if on_switch.is_pressed:
        while mode_switch.is_pressed:
            print('alg mode')
            sleep(0.1)
        while not mode_switch.is_pressed:
            print('simple mode')
            sleep(0.1)
