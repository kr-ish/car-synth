import obd
from changing_commands import COMMAND_NAMES
import time

connection = obd.OBD()  # auto-connects to USB or RF port

all_commands = obd.commands.__dict__

start_time = time.time()

with open('obd-log-{}.csv'.format(start_time), 'w') as f:

    while (True):
        for name in COMMAND_NAMES:
            cmd = all_commands[name]

            resp = connection.query(cmd, force=True)

            # When query fails it returns a blank OBDResponse() object
            if not resp.is_null():
                # print('{}, {}, {}, {}\n'.format(cmd.command, name, resp.value, resp.time - start_time, resp.time))
                f.write('{}, {}, {}, {}\n'.format(cmd.command, name, resp.value, resp.time - start_time, resp.time))
            else:
                print('null')
