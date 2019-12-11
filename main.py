import uinput
import time

events = (
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,
    )

device = uinput.Device(events)

x = 0
while True:
  x = x + 1
  device.emit(uinput.BTN_LEFT, 1)
  device.emit(uinput.BTN_LEFT, 0)
  
  device.emit(uinput.REL_Y, -180)
  
  device.emit(uinput.BTN_LEFT, 1)
  device.emit(uinput.BTN_LEFT, 0)
  time.sleep(0.0001)
  print(x)