[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)

## Part C - Modify our ```main.py``` to include stepper
**Synopsis:** We've added our driver code now we need to hook up our API so that 
the webapp can connect to it.

## Objectives
* Top of Main
* Environmental Sensor Gather Function
* API Routes for the Stepper
* API Routes for the PWM LED (to be done in class)

### Step C1: top of main.py
```python
#!/usr/bin/python
import time
import pprint
from stepper import PiStepper
from bmp280 import PiBMP280
from flask import *
app = Flask(__name__)

# Create a stepper motor controller object
pi_smc = PiStepper()

# create a pi bmp280 sensor object and data structure
env_sensor = {'name' : 'bmp280', 'addr' : 0x76, 'chip' : PiBMP280(0x76) , 'data' : {}}
```    

### Step C2: Environmental Sensors
```python
## function to read environmental parameters
def get_env_sensors():
    # Read the Sensor ID for 0x76 -> values into the ['data'] dictionary
    (chip_id, chip_version) = env_sensor['chip'].readBMP280ID()
    env_sensor['data']['chip_id'] = chip_id
    env_sensor['data']['chip_version'] = chip_version

    # Read the Sensor Temp/Pressure values into the ['data'] dictionary
    (temperature, pressure) = env_sensor['chip'].readBMP280All()
    env_sensor['data']['temperature'] = { 'reading': temperature, 'units' : 'C' }
    env_sensor['data']['pressure'] = { 'reading': pressure, 'units' : 'hPa' }
    return env_sensor['data']
```

### Step C3: API Route to kick off Webpage
```python
# ============================== API Routes ===================================
@app.route("/")
def index():
    return render_template('index.html')
    
```

### Step C4: API Routes for Stepper Motor
```python
# ============================= POST: /motor/<state> ============================
# control motor by POST methods from curl for example
# curl http://iot8e3c:5000/motor/0
# curl http://iot8e3c:5000/motor/1
# -----------------------------------------------------------------------------
@app.route("/motor/<int:motor_state>", methods=['GET'])
def motor(motor_state):
    if motor_state == 0:    # stop
        pi_smc.stop()
    elif motor_state == 1:      # start
        pi_smc.start()
    else:
        return ('Unknown Stepper Motor state!', 400)
    return ('', 204)


# ====================== GET: /motor_speed/<speed_rpm> ========================
# set the motor speed in RPM by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_speed/60
# -----------------------------------------------------------------------------
@app.route("/motor_speed/<int:motor_speed>", methods=['GET'])
def set_motor_speed(motor_speed):
    pi_smc.setSpeed(motor_speed)
    return "Set Motor Speed : " + str(pi_smc.getSpeed()) + "\n"

# ===================== GET: /motor_direction/<direction> =====================
# set the motor direction (CW/CCW) by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_direction/1
# -----------------------------------------------------------------------------
@app.route("/motor_zero", methods=['GET'])
def set_motor_zero():
    pi_smc.setPosition(0)
    return "Set Motor Position : " + str(pi_smc.getPosition()) + "\n"

# ===================== GET: /motor_direction/<direction> =====================
# set the motor direction (CW/CCW) by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_direction/1
# -----------------------------------------------------------------------------
@app.route("/motor_direction/<string:direction>", methods=['GET'])
def set_motor_dir(direction):
    pi_smc.setDirection(direction)
    return "Set Motor Direction : " + str(pi_smc.getDirection()) + "\n"

# ===================== GET: /motor_steps/<steps> =====================
# set the motor steps (int) by HTTP GET method  CURL example:
# curl http://iot8e3c:5000/motor_steps/100
# -----------------------------------------------------------------------------
@app.route("/motor_steps/<int:steps>", methods=['GET'])
def set_motor_steps(steps):
    pi_smc.setSteps(steps)
    return "Set Motor Steps : " + str(pi_smc.getSteps()) + "\n"

# ====================== GET: /motor_position/<position> ======================
# set the motor position by HTTP GET method. CURL example:
# curl http://iot8e3c:5000/motor_position/1
# -----------------------------------------------------------------------------
@app.route("/motor_position/<int:position>", methods=['GET'])
def set_motor_pos(position):
    pi_smc.setDirection(direction)
    return "Set Motor Direction : " + str(pi_smc.getDirection()) + "\n"


# ======================= POST: /motor_multistep/<dir> =========================
# set the motor multistep by POST method from curl. For example:
# curl --data 'steps=10&direction=CW' http://iot8e3c:5000/motor_multistep
# -----------------------------------------------------------------------------
@app.route("/motor_multistep", methods=['POST'])
def postMotorMultistep():
    ctrl_data = request.data
    print "Motor Control Data:" + ctrl_data
    direction = str(request.form['direction'])
    if (direction == 'CW'):
        pi_smc.setDirection(1)
    elif (direction == 'CCW'):      # start
        pi_smc.setDirection(0)
    else:
        return ('Unknown Stepper Motor Direction!', 400)

    steps = str(request.form['steps'])
    pi_smc.step(int(steps))

    return "Motor Multisteps Steps:" + steps + " Direction:"+ direction + "\n"
```

### Step C5: API Route for Server Sent Events + app_main
```python
# =========================== Endpoint: /myData ===============================
# read the sensor values by GET method from curl for example
# curl http://iot8e3c:5000/myData
# -----------------------------------------------------------------------------
@app.route('/myData')
def myData():
    def get_values():
        while True:
            # return the yield results on each loop, but never exits while loop
            data_obj = {'environmental' : get_env_sensors(),
                        'motor' : { 'position':str(pi_smc.getPosition()),
                                    'state':str(pi_smc.getState()) }
            }

            yield('data: {0}\n\n'.format(data_obj))
            time.sleep(2.0)
    return Response(get_values(), mimetype='text/event-stream')
# ============================== API Routes ===================================

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
# =============================================================================
```

[PART D](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartD.md) Refactor index.html and add Javascript Tabs

[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)
