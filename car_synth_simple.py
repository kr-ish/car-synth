import obd
from gpiozero import PWMLED
from time import sleep

# Setup OBD connection and commands
connection = obd.OBD()  # auto-connects
print(connection.status())
speed_cmd = obd.commands.SPEED
rpm_cmd = obd.commands.SPEED


vca = PWMLED(17, frequency=490)
vcf = PWMLED(18, frequency=490)
vco = PWMLED(22, frequency=490)
lfo = PWMLED(23, frequency=490)

vca_next_val = 0.0
vcf_next_val = 0.0
vco_next_val = 0.0
lfo_next_val = 0.0


while (True):
    speed_resp = connection.query(speed_cmd, force=True)
    if speed_resp.is_null():
        continue

    # rpm_resp = connection.query(rpm_cmd, force=True)
    # if rpm_resp.is_null():
    #     continue

    speed_val = float(speed_resp.value.split('kph')[0]) # 0 - 50 kph
    vco_next_value = speed_resp.value / 50.0
    vco_next_value = vco_next_value % 1.0
    vco.value = vco_next_value
    sleep(0.1)

