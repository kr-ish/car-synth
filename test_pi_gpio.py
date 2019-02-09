from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

led = PWMLED(17, frequency=490)
# button = Button(3)

# button.when_pressed = led.on
# button.when_released = led.off

# pause()

value = 0.0
while True:
    value += 0.05
    value = value % 1.0
    led.value = value
    sleep(0.1)

