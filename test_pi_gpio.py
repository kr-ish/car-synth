from gpiozero import LED, Button
from signal import pause
from time import sleep

led = PWMLED(17)
# button = Button(3)

# button.when_pressed = led.on
# button.when_released = led.off

# pause()

while True:
    led.value += 0.05
    led.value = led.value % 1.0
    sleep(1)
    