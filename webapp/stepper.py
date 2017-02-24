import RPi.GPIO as GPIO
import time

LED     = 23    # GPIO23 RUNNING STATUS LED
SW      = 25    # cobbler pin 22 (GPIO25)

AIN1    = 19    # GPIO19 TB6612 AIN1 Logic Input
AIN2    = 26    # GPIO26 TB6612 AIN2 Logic Input
BIN1    = 20    # GPIO20 TB6612 BIN1 Logic Input
BIN2    = 21    # GPIO21 TB6612 BIN2 Logic Input
STBY    = 16    # GPIO16 TB6612 Standby Input

# =============================================================================
# create a Stepper Motor Object
# -----------------------------------------------------------------------------
class PiStepper(object):
    """Raspberry Pi 'IoT GPIO Stepper Motor'."""

    def __init__(self, freq=10, steps=600):
        self.steps_per_rev = steps
        self.sec_per_step = 0.1
        self.steppingcounter = 0
        self.currentstep = 0
        self.speed = 0
        self.state = 0
        self.steps = 0
        self.direction = 0
        self.position = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)          # BMC Pin numbering convention
        GPIO.setup(LED, GPIO.OUT)       # LED as output
        GPIO.setup(AIN1, GPIO.OUT)      # AIN1 as output
        GPIO.setup(AIN2, GPIO.OUT)      # AIN2 as output
        GPIO.setup(BIN1, GPIO.OUT)      # BIN1 as output
        GPIO.setup(BIN2, GPIO.OUT)      # BIN2 as output
        GPIO.setup(STBY, GPIO.OUT)      # Standby as output
        GPIO.output(AIN1,0)             # initialize AIN1 state to off
        GPIO.output(AIN2,0)             # initialize AIN2 state to off
        GPIO.output(BIN1,0)             # initialize BIN1 state to off
        GPIO.output(BIN2,0)             # initialize BIN2 state to off
        GPIO.output(STBY,0)             # initialize Standby state to off
        GPIO.setup(SW,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #  import pdb; pdb.set_trace()

    def hello(self):
        print "Hello Stepper"

    def start(self):
        # add code

    def stop(self):
        # add code

    def getState(self):
        # add code

    # get motor position
    def getPosition(self):
        # add code

    # set motor position
    def setPosition(self,position):
        # add code

    # set the speed parameters for stepper motor based on RPM
    def setSpeed(self, rpm):
        # add code

    def getSpeed(self):
        # add code

    # perform one step in sequence at a direction CW or CCW
    def oneStep(self, direction):
        # add code

    # set current pin in sequence
    def setPin(self, pin, value):
        # add code

    # set motor direction
    def setDirection(self,direction):
        # add code

    # get motor direction
    def getDirection(self):
        return self.direction

    # set motor steps
    def setSteps(self,steps):
        # add code

    # get motor direction
    def getSteps(self):
        # add code

    # execute all steps
    def step(self, steps):
        # add code

    # de-energize all coils
    def nullCoils(self):
        # add code
