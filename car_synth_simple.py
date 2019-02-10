import obd
from gpiozero import PWMLED
from time import sleep

# Setup OBD connection and commands
connection = obd.OBD()  # auto-connects
print(connection.status())

speed_cmd = obd.commands.SPEED  # 0-50 kph, 0-120 kph in data
rpm_cmd = obd.commands.RPM  #  400 to 2200 RPM in data
throttle_cmd = obd.commands.THROTTLE_POS  # throttle 0-40 % in data
fuel_trim_cmd = obd.commands.LONG_FUEL_TRIM_1  # -5 to 8 % in data

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

    # Throttle to VCA
    throttle_resp = connection.query(throttle_cmd, force=True)
    if not throttle_resp.is_null():
        throttle_val = float(throttle_resp.value.magnitude)
        vca_next_value = throttle_val / 50.0
        vca.value = vca_next_value


    # RPM to VCF
    rpm_resp = connection.query(rpm_cmd, force=True)
    if not rpm_resp.is_null():
        rpm_val = float(rpm_resp.value.magnitude)
        vcf_next_value = (rpm_val - 400.0) / 1900.0
        vcf.value = vcf_next_value

    # Speed to VCO
    speed_resp = connection.query(speed_cmd, force=True)
    if not speed_resp.is_null():
        print(speed_resp.value, type(speed_resp.value))
        speed_val = float(speed_resp.value.magnitude)
        vco_next_value = speed_val / 100.0
        if vco_next_value > 1.0:
            vco_next_value = 1.0
        print(vco_next_value)
        vco.value = vco_next_value
    else:
        print('speed null')

    # Fuel Trim to LFO
    fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
    if not fuel_trim_resp.is_null():
        fuel_trim_val = float(fuel_trim_resp.value.magnitude)
        lfo_next_value = abs(fuel_trim_val) / 8.0
        lfo.value = lfo_next_value
