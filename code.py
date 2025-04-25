import time
import board
import busio
import usb_hid
import adafruit_mpu6050
from adafruit_hid.mouse import Mouse
import digitalio

mouse = Mouse(usb_hid.devices)

SCL = board.GP1
SDA = board.GP0
button_pin_LEFT = board.GP2
button_pin_RIGHT = board.GP3

# Initialize I2C (GP0 = SDA, GP1 = SCL)
i2c = busio.I2C(scl=SCL, sda=SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Button connected to GP2 pin
button_left = digitalio.DigitalInOut(button_pin_LEFT)
button_left.direction = digitalio.Direction.INPUT
button_left.pull = digitalio.Pull.UP  # Enable internal pull-up resistor

# Button connected to GP3 pin
button_right = digitalio.DigitalInOut(button_pin_RIGHT)
button_right.direction = digitalio.Direction.INPUT
button_right.pull = digitalio.Pull.UP  # Enable internal pull-up resistor

tm = 0.01  # time.sleep(0.01)

# Calibration and settings for the motion sensor
sensitivity = 1.5  # Adjust motion sensitivity (lower = more sensitive)

spanmax = 1.5
spanmin = 0

while True:
    # Get acceleration data from MPU6050
    accel = mpu.acceleration  # acceleration data on x, y, z axes

    accel = [int(accel[0]), int(accel[1]), 0]  # stabilize by converting to int and ignoring z

    # If within a specific range, do not move
    if (((abs(accel[0]) >= spanmin and abs(accel[0]) <= spanmax) and
         (abs(accel[1]) >= spanmin and abs(accel[1]) <= spanmax))):
        time.sleep(tm)
        continue

    else:
        # Convert X and Y to int and multiply with sensitivity
        X_move = int(accel[0] * sensitivity)
        Y_move = int(accel[1] * sensitivity)
        mouse.move(x=-X_move, y=-Y_move)

    # Right click will be added here
	# Left click will be added here

    time.sleep(tm)
