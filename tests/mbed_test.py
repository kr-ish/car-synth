from mbedrpc import *

mbed = HTTPRPC("192.168.0.4")

x = DigitalOut(mbed,"LED1") # These objects should already exist on mbed
z = DigitalOut(mbed,"LED2") 
ain = AnalogIn(mbed, "LED3")

x.write(1)
z.write(0.5)
ain.read()

# interface = mbed_interface(mbed, "interface")
# interface.new("DigitalOut",led2, "LED2") #new(Class, Name, Pin)
# y = DigitalOut(mbed, "led2") #The second parameter should match the name given above
# x.read()
# y.write(1)

