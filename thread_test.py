from time import sleep
from random import random
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

    # vco_next_value = (speed_val / 100 + .3) + \
    #     ((random() - .5) * (3.0/5)) * (rpm_val  - 480) / 1720
    # if vco_next_value > 1.0:
    #     vco_clipped_value = 1.0
    # elif vco_next_value < 0:
    #     vco_clipped_value = 0.0
    # else:
    #     vco_clipped_value = vco_next_value
    # print('vco_next_value {}, vco_clipped_value {}'.format(vco_next_value, vco_clipped_value))

    # vca_next_value = vco_clipped_value + 0.1
    # if vca_next_value > 1.0:
    #     vca_clipped_value = 1.0
    # else:
    #     vca_clipped_value = vca_next_value
    # print('vca_next_value {}, vca_clipped_value {}'.format(vca_next_value, vca_clipped_value))

    # lfo_next_value = (rpm_val - 480) / 1720
    # if lfo_next_value > 1.0:
    #     lfo_clipped_value = 1.0
    # elif lfo_next_value < 0:
    #     lfo_clipped_value = 0.0
    # else:
    #     lfo_clipped_value = lfo_next_value
    # print('lfo_next_value {}, lfo_clipped_value {}'.format(lfo_next_value, lfo_clipped_value))

    # sleep_val = (1.0 - (speed_val / 100)) * 0.3
    # print('sleep val {}'.format(sleep_val))
    # sleep(sleep_val)
    sleep(0.1)
