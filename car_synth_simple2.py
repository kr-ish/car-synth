import obd
from gpiozero import PWMLED
from time import sleep
from random import random

# Setup OBD connection and commands
# connection = obd.OBD()  # auto-connects
# print(connection.status())

speed_cmd = obd.commands.SPEED  # 0-50 kph, 0-120 kph in data
rpm_cmd = obd.commands.RPM  #  400 to 2200 RPM in data
throttle_cmd = obd.commands.THROTTLE_POS  # throttle 0-40 % in data
fuel_trim_cmd = obd.commands.SHORT_FUEL_TRIM_1  # -5 to 8 % in data

# Setup GPIO
vca = PWMLED(17, frequency=490)
vcf = PWMLED(18, frequency=490)
vco = PWMLED(22, frequency=490)
lfo = PWMLED(23, frequency=490)

# GPIO update vars
vca_next_val = 0.0
vcf_next_val = 0.0
vco_next_val = 0.0
lfo_next_val = 0.0
vca_clipped_val = 0.0
vcf_clipped_val = 0.0
vco_clipped_val = 0.0
lfo_clipped_val = 0.0


# main
while (True):

    # Speed + RPM to VCO
    # speed_resp = connection.query(speed_cmd, force=True)
    # fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
    # rpm_resp = connection.query(rpm_cmd, force=True)

    # if speed_resp.is_null():
    #     print('speed_resp null')
    #     continue
    # elif rpm_resp.is_null():
    #     print('rpm_resp null')
    #     continue
    # elif fuel_trim_resp.is_null():
    #     print('fuel_trim_resp null')
    #     continue

    # speed_val = float(speed_resp.value.magnitude)
    # rpm_val = float(rpm_resp.value.magnitude)
    # fuel_trim_val = float(fuel_trim_resp.value.magnitude)
    speed_val = 60
    rpm_val = 2000
    fuel_trim_val = 5.0


    vco_next_value = (speed_val / 160 + .3) + \
        ((random() - .5) * (3.0/5)) * (rpm_val  - 480) / 1720
    # vco_next_value = (speed_val / 160 + .3) \
    #     + ((fuel_trim_val + 9) / 20 - .5) * (3.0/5) * (rpm_val  - 480) / 1720
    if vco_next_value > 1:
        vco_clipped_value = 1.0
    elif vco_next_value < 0:
        vco_clipped_value = 0.0
    else:
        vco_clipped_value = vco_next_value
    print('vco_next_value {}, vco_clipped_value {}'.format(vco_next_value, vco_clipped_value))
    vco.value = vco_clipped_value

    # Fuel Trim to LFO
    lfo_next_value = (rpm_val - 480) / 1720
    if lfo_next_value > 1:
        lfo_clipped_value = 1.0
    elif lfo_next_value < 0:
        lfo_clipped_value = 0.0
    else:
        lfo_clipped_value = lfo_next_value
    print('lfo_next_value {}, lfo_clipped_value {}'.format(lfo_next_value, lfo_clipped_value))
    lfo.value = lfo_clipped_value
    sleep(0.07)
