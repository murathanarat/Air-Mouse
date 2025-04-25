🖱️ Motion-Controlled Mouse with MPU6050 and Raspberry Pi RP2040-Zero
This project allows you to control your computer's mouse using a Raspberry Pi RP2040-Zero and an MPU6050 motion sensor.
The cursor is moved based on the accelerometer data received from the sensor.

📦 Requirements
Raspberry Pi RP2040-Zero

MPU6050 Accelerometer/Gyroscope Sensor

CircuitPython firmware (adafruit-circuitpython-raspberry_pi_pico-tr-9.2.7)

Required libraries like adafruit_hid and adafruit_mpu6050
(you can simply copy and paste the lib folder)

(Optional) 2 buttons for click functionality

🚀 Setup Steps
1. Install CircuitPython
Download and flash the CircuitPython firmware for the RP2040-Zero:
adafruit-circuitpython-raspberry_pi_pico-tr-9.2.7

2. Copy the Libraries
After flashing, your computer will recognize the board as a USB drive named CIRCUITPY.

Open the lib folder on the drive.

Copy the necessary libraries from the downloaded lib folder into this directory
(e.g., adafruit_hid, adafruit_mpu6050)
(You can just copy and paste the entire lib folder.)

3. Add the Code File
Create a file named code.py in the root of the CIRCUITPY drive.

Paste your motion control Python script into it and save.

4. Run the Project
Press the reset button on the Raspberry Pi RP2040-Zero.

The code will start running automatically.

Now you can move the MPU6050 sensor to control the mouse cursor!

🛠️ Notes
You can fine-tune cursor behavior by adjusting values like sensitivity, spanmin, and spanmax in the code.

Make sure the sensor is connected to the correct I2C pins (default: SDA=GP0, SCL=GP1).

You can also add click functionality later by connecting a button to pin GP2.