"""Tests OBD connection and prints all available commands."""

import obd

connection = obd.OBD()  # auto-connects to USB or RF port

all_commands = obd.commands.__dict__
all_command_names = all_commands.keys()

for name in all_command_names:
    cmd = all_commands[name]

    # TODO: try without?
    # if isinstance(cmd, list):
    #     continue

    resp = connection.query(cmd, force=True)

    # When query fails it returns a blank OBDResponse() object
    # if resp is not None and resp.value is not None:
    if not resp.is_null():
        print '{}: {} - {}'.format(name, cmd, resp.value, resp.messages)
