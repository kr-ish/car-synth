import obd
# from obd import OBDStatus

connection = obd.OBD() # auto-connects to USB or RF port

# cmd = obd.commands.THROTTLE_POS # select an OBD command (sensor)
cmd = obd.commands.SPEED # select an OBD command (sensor)
# cmd = obd.commands.MONITOR_HEATED_CATALYST_B3 # select an OBD command (sensor)
# cmd = obd.commands.GET_CURRENT_DTC



while (True):
    print(connection.status())
    response = connection.query(cmd, force=True) # send the command, and parse the response
    print(response.value) # returns unit-bearing values thanks to Pint
    # print(response.value.to("mph")) # user-friendly unit conversions
