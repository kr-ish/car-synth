"""Quick test to check if pi GPIO is working."""

from gpiozero import PWMLED, Button
from time import sleep

out_1 = PWMLED(17, frequency=490)
out_2 = PWMLED(18, frequency=490)
out_3 = PWMLED(22, frequency=490)
out_4 = PWMLED(23, frequency=490)

value = 0.0
while True:
    value += 0.05
    value = value % 1.0
    out_1.value = value
    out_2.value = value
    out_3.value = value
    out_4.value = value
    sleep(0.1)
