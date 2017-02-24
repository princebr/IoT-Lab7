[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)

## Part A - Check Starter Files, Sensors and PWM
**Synopsis:** In this part, we will re-test that the BMP280 sensor is still 
operating correctly and also run the pre-coded unit test for LED PWM control. 
Due to the amount of code needed to operate the stepper motor, the LED PWM 
driver and unit test are provided for this lab.

## Objectives
* Check to ensure all starter files are present in the lab
* Run the BMP280 temperature and pressure sensor unit test
* Run the LED PWM unit test

### Step A1: Check starter files
```sh

pi$ git pull (from iot110-student REPO, then copy to your working folder)

pi$ cd webapp
pi$ tree  .
.
├── bmp280.py
├── main.py
├── pwm.py
├── pwm_test.py
├── static
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── jquery-ui.min.css
│   │   ├── jquery-ui.theme.min.css
│   │   ├── lab7.css
│   │   └── morris.css
│   ├── icon
│   │   └── favicon.ico
│   └── js
│       ├── bootstrap.min.js
│       ├── jquery-3.1.1.min.js
│       ├── jquery-ui.min.js
│       ├── lab7.js
│       ├── morris.min.js
│       └── raphael.min.js
├── stepper.py
├── stepper_test.py
└── templates
    └── index.html

```    

### Step A2: Run BMP280 Unit Test
```python
# =============================================================================
# main to test from CLI
def main():

    # create an instance of my pi bmp280 sensor object
    pi_bmp280 = PiBMP280()

    # Read the Sensor ID.
    (chip_id, chip_version) = pi_bmp280.readBMP280ID()
    print "    Chip ID :", chip_id
    print "    Version :", chip_version

    # Read the Sensor Temp/Pressure values.
    (temperature, pressure) = pi_bmp280.readBMP280All()
    print "Temperature :", temperature, "C"
    print "   Pressure :", pressure, "hPa"

if __name__=="__main__":
   main()
# =============================================================================

# -----------------------------------------------------------------------------
pi$ ./bmp280
    Chip ID : 88
    Version : 1
Temperature : 24.78 C
   Pressure : 1006.53054419 hPa
# -----------------------------------------------------------------------------
```    

### Step A3: Run LED PWM Unit Test
```python
# =============================================================================
#!/usr/bin/python

import time
from pwm import PiPwm

PWM0 = 0    # logical handle for RPi3 PWM0
PWM1 = 1    # logical handle for RPi3 PWM1
# create an instance of my pi thing.
pi_pwm = PiPwm()

# Create two counter breathing PWM LEDs
print('Connect RED LED to GPIO18, GREEN LED to GPIO13, DIR SW to GPIO25')

time.sleep(1.0)
print('Starting PWM0 at 5Hz with 75% duty cycle')
ch0 = pi_pwm.start_pwm(0, 5, 75)
# time.sleep(0.01)
print('Starting PWM1 at 3Hz with 10% duty cycle')
ch1 = pi_pwm.start_pwm(1, 5, 10)

time.sleep(10.0)
print('Stopping PWM0')
pi_pwm.stop_pwm(ch0)
time.sleep(3.0)
print('Stopping PWM1')
pi_pwm.stop_pwm(ch1)
# =============================================================================

(review the pwm.py driver in Atom)

$pi ./pwm_test.py
Connect RED LED to GPIO18, GREEN LED to GPIO13, DIR SW to GPIO25
Starting PWM0 at 5Hz with 75% duty cycle
Starting PWM1 at 3Hz with 10% duty cycle
Stopping PWM0
Stopping PWM1
```    

[PART B](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartB.md) Develop stepper.py and unit test

[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)
