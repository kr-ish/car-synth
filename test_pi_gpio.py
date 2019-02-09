from gpiozero import LED, Button
from signal import pause
from time import sleep

led = PWMLED(17)
# button = Button(3)

# button.when_pressed = led.on
# button.when_released = led.off

# pause()

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
