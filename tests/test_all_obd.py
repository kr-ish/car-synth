import obd
from command_names import COMMAND_NAMES

connection = obd.OBD() # auto-connects to USB or RF port


# TODO: try in interactive mode??
# connection.print_commands()


all_commands = obd.commands.__dict__
all_command_names = all_commands.keys()

# TODO: try
# all_command_names = COMMAND_NAMES

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
