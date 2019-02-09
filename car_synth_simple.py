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
    speed_resp = connection.query(speed_cmd, force=True)
    if speed_resp.is_null():
        print('speed_resp null')
        continue
    speed_val = float(speed_resp.value.split()[0])
    vco_next_value = speed_resp.value / 100.0
    vco.value = vco_next_value

    # # Fuel Trim to LFO
    # fuel_trim_resp = connection.query(fuel_trim_cmd, force=True)
    # if fuel_trim_resp.is_null():
    #     print('fuel_trim_resp null')
    #     continue
    # fuel_trim_val = float(fuel_trim_resp.value.split()[0])
    # lfo_next_value = abs(fuel_trim_resp.value) / 8.0
    # lfo.value = lfo_next_value
