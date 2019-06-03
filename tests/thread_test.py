"""Test code used to check that threading the OBD read worked as intended."""

from time import sleep
import thread

# GPIO update vars
vca_next_val = 0.0
vcf_next_val = 0.0
vco_next_val = 0.0
lfo_next_val = 0.0
vca_clipped_val = 0.0
vcf_clipped_val = 0.0
vco_clipped_val = 0.0
lfo_clipped_val = 0.0

speed_val = 0.0
rpm_val = 400.0

def read_obd():
    global speed_val
    global rpm_val

    while(True):
        speed_val = (speed_val + 1) % 100
        rpm_val = (rpm_val + 100) % 2200
        sleep(1)


# main
thread.start_new_thread(read_obd, ())

while (True):

    print('speed_val {}, rpm_val {}'.format(speed_val, rpm_val))
    sleep(0.1)
