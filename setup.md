[IOT STUDENT HOME](https://gitlab.com/iot110/iot110-student/blob/master/README.md)

## Setting up Lab7

**Synopsis:** For this lab we will continue building on our IoT suite by creating
a web app for ACTUATORS.  For our Lab ACTUATORS we will be using 2 LEDs with a
dimming function created by pulse width modulation (PWM) and an automotive
instrument analog indicator using a precision stepper motor and the TB6612 Driver module.

### Objectives
* Test to ensure BMP280 sensor and driver are still working correctly (no code change)
* Test to ensure PWM LEDs and driver are working correctly (driver and unit test provided)
* Build a driver ```stepper.py``` for the motor and test (unit test provided)
* Interface the main Flask webapp ```main.py``` to the stepper and PWM drivers
* Add new HTML code for the PWM slider controls and stepper motor control.
* Add JavaScript code to add actuator control and status as well as sensing.

The various steps of this lab are summarized as:
* [PART A](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartA.md) Test BMP280 and PWM LEDs
* [PART B](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartB.md) Develop stepper.py and unit test
* [PART C](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartC.md) Modify main.py for stepper and PWM control code
* [PART D](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartD.md) Refactor ```index.html``` and add Javascript Tabs

[IOT STUDENT HOME](https://gitlab.com/iot110/iot110-student/blob/master/README.md)
