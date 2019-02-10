import obd
from gpiozero import PWMLED
from time import sleep
import random

# Setup OBD connection and commands
connection = obd.OBD()  # auto-connects
print(connection.status())

speed_cmd = obd.commands.SPEED
rpm_cmd = obd.commands.SPEED
throttle_cmd = obd.commands.THROTTLE_POS
fuel_trim_cmd = obd.commands.LONG_FUEL_TRIM_1

# TODO: add ranges


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


# main
while (True):

    # # Throttle to VCA
    # throttle_resp = connection.query(throttle_cmd, force=True)
    # if throttle_resp.is_null():
    #     print('throttle_resp null')
    #     continue
    # throttle_val = float(throttle_resp.value.split()[0])
    # vca_next_value = throttle_resp.value / 50.0
    # vca.value = vca_next_value


    # # RPM to VCF
    # rpm_resp = connection.query(rpm_cmd, force=True)
    # if rpm_resp.is_null():
    #     print('rpm_resp null')
    #     continue
    # rpm_val = float(rpm_resp.value.split()[0])
    # vcf_next_value = (rpm_resp.value - 400.0) / 1900.0
    # vcf.value = vcf_next_value

    # Speed to VCO
    # speed_resp = connection.query(speed_cmd, force=True)
    # if speed_resp.is_null():
    #     print('speed_resp null')
    #     continue
    # speed_val = float(speed_resp.value.split()[0])
    # vco_next_value = speed_resp.value / 100.0
    # vco.value = vco_next_value

    # # Fuel Trim to LFO
    # fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
    # if fuel_trim_resp.is_null():
    #     print('fuel_trim_resp null')
    #     continue
    # fuel_trim_val = float(fuel_trim_resp.value.split()[0])
    # lfo_next_value = abs(fuel_trim_resp.value) / 8.0
    # lfo.value = lfo_next_value

        # Speed + RPM to VCO
     speed_resp = connection.query(speed_cmd, force=True)
     fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
     rpm_resp = connection.query(rpm_cmd, force=True)
     if speed_resp.is_null():
         print('speed_resp null')
         continue
     elif rpm_resp.is_null():
         print('rpm_resp null')
         continue
     elif fuel_trim_resp.is_null():
         print('fuel_trim_resp null')
         continue
     speed_val = float(speed_resp.value.split()[0])
     rpm_val = float(rpm_resp.value.split()[0])
     fuel_trim_val = float(fuel_trim_resp.value.split()[0])
     #vco_next_value = (speed_val / 100 + .3) + ((random.rand() - .5) * (3.0/5)) * (rpm_val  - 480) / 1720
     vco_next_value = (speed_val / 100 + .3) + ((fuel_trim_val + 9) / 20 - .5) * (3.0/5) * (rpm_val  - 480) / 1720
     if vco_next_value > 1:
        vco_next_value = 1.0
     elif vco_next_value < 0:
        vco_next_value = 0.0
     vco.value = vco_next_value

    # Fuel Trim to LFO
    # fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
    # if fuel_trim_resp.is_null():
    #     print('fuel_trim_resp null')
    #     continue
    # fuel_trim_val = float(fuel_trim_resp.value.split()[0])
    lfo_next_value = (rpm_val - 480) / 1720
    lfo.value = lfo_next_value

