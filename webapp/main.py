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
# import pdb; pdb.set_trace()

## function to read environmental parameters
def get_env_sensors():
    # Read the Sensor ID for 0x76 -> values into the ['data'] dictionary
    # ... add code ....

    # Read the Sensor Temp/Pressure values into the ['data'] dictionary
    # ... add code ....
    return env_sensor['data']

@app.route("/")
def index():
    return render_template('index.html')
# ============================== API Routes ===================================
# ============================= POST: /motor/<state> ============================
# get sensor values methods from curl for example
# curl http://iot8e3c:5000/sensors
# -----------------------------------------------------------------------------
@app.route("/sensors", methods=['GET'])
def sensors():
    # return "Sensors" + str(get_env_sensors()) + "\n"
    # pprint.pprint(get_env_sensors())
    return "Sensors" + "\n"

# ============================= POST: /motor/<state> ============================
# control motor by POST methods from curl for example
# curl http://iot8e3c:5000/motor/0
# curl http://iot8e3c:5000/motor/1
# -----------------------------------------------------------------------------
@app.route("/motor/<int:motor_state>", methods=['GET'])
def motor(motor_state):
    # ... add code ....
    return ('', 204)


# ====================== GET: /motor_speed/<speed_rpm> ========================
# set the motor speed in RPM by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_speed/60
# -----------------------------------------------------------------------------
@app.route("/motor_speed/<int:motor_speed>", methods=['GET'])
def set_motor_speed(motor_speed):
    # ... add code ....
    return "Set Motor Speed : " + str(pi_smc.getSpeed()) + "\n"

# ===================== GET: /motor_direction/<direction> =====================
# set the motor direction (CW/CCW) by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_direction/1
# -----------------------------------------------------------------------------
@app.route("/motor_zero", methods=['GET'])
def set_motor_zero():
    # ... add code ....
    return "Set Motor Position : " + str(pi_smc.getPosition()) + "\n"

# ===================== GET: /motor_direction/<direction> =====================
# set the motor direction (CW/CCW) by GET method from curl. For example:
# curl http://iot8e3c:5000/motor_direction/1
# -----------------------------------------------------------------------------
@app.route("/motor_direction/<string:direction>", methods=['GET'])
def set_motor_dir(direction):
    # ... add code ....
    return "Set Motor Direction : " + str(pi_smc.getDirection()) + "\n"

# ===================== GET: /motor_steps/<steps> =====================
# set the motor steps (int) by HTTP GET method  CURL example:
# curl http://iot8e3c:5000/motor_steps/100
# -----------------------------------------------------------------------------
@app.route("/motor_steps/<int:steps>", methods=['GET'])
def set_motor_steps(steps):
    # ... add code ....
    return "Set Motor Steps : " + str(pi_smc.getSteps()) + "\n"

# ====================== GET: /motor_position/<position> ======================
# set the motor position by HTTP GET method. CURL example:
# curl http://iot8e3c:5000/motor_position/1
# -----------------------------------------------------------------------------
@app.route("/motor_position/<int:position>", methods=['GET'])
def set_motor_pos(position):
    # ... add code ....
    return "Set Motor Direction : " + str(pi_smc.getDirection()) + "\n"


# ======================= POST: /motor_multistep/<dir> =========================
# set the motor multistep by POST method from curl. For example:
# curl --data 'steps=10&direction=CW' http://iot8e3c:5000/motor_multistep
# -----------------------------------------------------------------------------
@app.route("/motor_multistep", methods=['POST'])
def postMotorMultistep():
    # ... add code ....

    return "Motor Multisteps Steps:" + steps + " Direction:"+ direction + "\n"

# curl --data 'mykey=FOOBAR' http://0.0.0.0:5000/createHello
# echo 'mykey={"name":"Carrie Fisher","age":"60"}' | curl -d @- http://0.0.0.0:5000/createHello
@app.route('/test', methods = ['POST'])
def postRequestTest():
    mydata = request.data

    # import pdb; pdb.set_trace()
    return "Hello API Server : You sent a "+ request.method + \
            " message on route path " + request.path + \
            " \n\tData:" +  data + "\n"


# ============================ END API Routes =================================

# ============================= Run App Server ================================
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
