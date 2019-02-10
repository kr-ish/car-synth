import obd
from gpiozero import PWMLED
from time import sleep

# Setup OBD connection and commands
connection = obd.OBD()  # auto-connects
print(connection.status())

cmd = obd.commands.SPEED  # 0-50 kph, 0-120 kph in data
# cmd = obd.commands.RPM  #  400 to 2200 RPM in data
# cmd = obd.commands.THROTTLE_POS  # throttle 0-40 % in data
# cmd = obd.commands.LONG_FUEL_TRIM_1  # -5 to 8 % in data

# Setup GPIO
out_pin = PWMLED(22, frequency=490)

# GPIO update vars
next_val = 0

while (True):

    resp = connection.query(cmd, force=True)

    if resp.is_null():
        print('null')
    else:
        next_value = float(resp.value.magnitude)
        next_value = next_value / 100.0
        if next_value > 1.0:
            next_value = 1.0
        elif next_value = 0.0:
            next_value = 0.0
        print(next_value)

        vco.value = next_value        
