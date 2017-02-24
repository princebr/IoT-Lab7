[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)

## Part D - Add JavaScript for Stepper/PWM Control and Temp/Pressure Sensor
**Synopsis:** We have all of our low level tools integrated and tested.  Now it's
time to modify our webpage (```index.html```) and the associated (```lab7.js```) 
JavaScript that provides all the interface and dynamic behavior.

## Objectives
* Add additional Tabs and Concent to ```index.html```
* Add Stepper Motor functionality to lab7.js
* Add PWM LED dimmer control to lab7.js

### Step D1: Webapp head section
Ensure all libraries are correctly ordered in ```<head>``` section.
```html
<head>
  <meta charset="utf-8">
  <title>UW IoT Lab7</title>

  <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/morris.css') }}">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/jquery-ui.min.css') }}">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/bootstrap.min.css') }}">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/lab7.css') }}">
  <link rel="shortcut icon" type="image/x-icon" href="{{ url_for('static',filename='icon/favicon.ico') }}">

  <script src="{{ url_for('static',filename='js/jquery-3.1.1.min.js') }}"></script>
  <script src="{{ url_for('static',filename='js/bootstrap.min.js') }}"></script>
  <script src="{{ url_for('static',filename='js/raphael.min.js') }}"></script>
  <script src="{{ url_for('static',filename='js/morris.min.js') }}"></script>
  <script src="{{ url_for('static',filename='js/jquery-ui.min.js') }}"></script>
  <script src="{{ url_for('static',filename='js/lab7.js') }}"></script>

</head>
```    

### Step D2: Tabs List Items
```html
                <li><a href="#tabs-environmental-data">EnvironTable</a></li>
                <li><a href="#tabs-stepper">STEPPER</a></li>
                <li><a href="#tabs-ledpwm">PWM LEDS</a></li>
```

### Step D3: Table for Temperature and Pressure
```html
                <table class="table table-hover table-striped">
                  <tr class=param-header>
                    <th>Time (PST)</th>
                    <th>Temperature (&degC)</th>
                    <th>Pressure (mbar)</th>
                  </tr>
                  <tr class=env-param-row>
                  </tr>
                  <tr class=env-param-row>
                  </tr>
                  <tr class=env-param-row>
                  </tr>
                  <tr class=env-param-row>
                  </tr>
                </table>
```

### Step D4: Table for Stepper Controls
```html
                <table>
                  <tr>
                    <td>
                      <!-- <div class="container well"> -->
                        <table class="table">
                          <tr>
                            <td><h6>Motor Status  <span id='motor_state' class="label label-default">&#8635</span></h6></td>
                          </tr>
                          <tr>
                            <td><h6>Motor Position(steps)  <span id="motor_position" class="label label-default">100</span></h6></td>
                          </tr>
                        </table>
                      <!-- </div> -->
                    </td>
                    <td>
                      <table class="table">
                        <tr>
                          <td>New Motor Speed(rpm):</td>
                          <td><input id='motor_speed' type="number" min="0" max="250" name="rpm" value=100></td>
                        </tr>
                        <tr>
                          <td>Number of Steps:</td>
                          <td><input id='motor_steps' type="number" min="0" max="600" name="steps" value=100></td>
                        </tr>
                        <tr>
                          <td>Motor Direction:</td>
                          <td><select id='motor_direction' type="text" name="direction" value="CW">
                                <option value="CW">Clockwise</option>
                                <option value="CCW">Counter Clockwise</option>
                              </select>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
```

### Step D5: Buttons for Stepper Commands
```html
                <div id="stepper_buttons" class="container well">
                  <button type='button' class="btn btn-default" id='motor_start'>START</button>
                  <button type='button' class="btn btn-default" id='motor_stop'>STOP</button>
                  <button type='button' class="btn btn-default" id='motor_zero'>POS ZERO</button>
                  <button type='button' class="btn btn-success" id='motor_multistep'>MULTI-STEP</button>
                </div>
```

### Step D6: Table for PWM LED Sliders
```html
                <table>
                  <tr>
                    <td class="slider-col">
                      <p>
                        <h4>RED LED</h4>
                        DUTY CYCLE (%) <input type="text" id="pwm1" readonly>
                      </p>
                      <div id="slider1"></div>
                    </td>
                    <td class="slider-col">
                      <p>
                        <h4>GREEN LED</h4>
                        DUTY CYCLE (%) <input type="text" id="pwm2" readonly>
                      </p>
                      <div id="slider2"></div>
                    </td>
                  </tr>
                </table>
```

### Step D7: Code for RED LED Slider
```javascript
  $( "#slider1" ).slider({
    orientation: "vertical",
    range: "min",
    min: 0,
    max: 100,
    value: 50,
    animate: true,
    slide: function( event, ui ) {
      $( "#pwm1" ).val( ui.value );
      console.log("red led duty cycle(%):",ui.value);
    }
  });
  
```

### Step D8: Code for RED LED Slider
```javascript
  $( "#slider2" ).slider({
    orientation: "vertical",
    range: "min",
    min: 0,
    max: 100,
    value: 50,
    animate: true,
    slide: function( event, ui ) {
      $( "#pwm2" ).val( ui.value );
      console.log("grn led duty cycle(%):",ui.value);
    }
  });
```

### Step D9: Code for Environmental Sensor Tables
```javascript
  // ============================== ENV TABLE =================================
  updateEnvironmentalTableData = (function (d) {
    var env = d;
    var timedata = getDateNow();
    env['date'] = timedata.date;
    env['time'] = timedata.time;

    env_table_data.push(env);
    if (env_table_data.length > 4) {
      env_table_data.shift();
      clearEnvTables();
      updateEnvironmentalTable(env_table_data);
    }
  });

  function updateEnvironmentalTable(data) {
    $('tr.env-param-row').each(function(i) {
      var tm = '<td>' + data[i].date + '</td>';
      var t = '<td>' + data[i]['environmental']['temperature'].reading.toFixed(2) + '</td>';
      var p = '<td>' + data[i]['environmental']['pressure'].reading.toFixed(2) + '</td>';
      $(this).append(tm);
      $(this).append(t);
      $(this).append(p);
    });
  }
  function clearEnvTables() {
    $('tr.env-param-row').each(function(i) {
      $(this).empty();
    });
  }
  // ============================== ENV TABLE =================================
```

### Step D10: Code for Stepper Motor Control
```python
  // ============================ STEPPER MOTOR ===============================
  // Buttons
  $('#motor_start').click(function() {
    console.log('Start Motor Up!');
    $.get('/motor/1');
  });
  $('#motor_stop').click(function() {
    console.log('Stop Motor');
    $.get('/motor/0');
  });
  $('#motor_zero').click(function() {
    console.log('Zero Motor Position');
    $.get('/motor_zero');
  });
  $('#motor_multistep').click(function() {
    var params = 'steps='+$('#motor_steps').val()+"&direction="+$('#motor_direction').val();
    console.log('Multistep with params:' + params);
    $.post('/motor_multistep', params, function(data, status){
                console.log("Data: " + data + "\nStatus: " + status);
            });
  });

  // Text Fields
  $('#motor_speed').change(function() {
    console.log('Changed motor speed to ' + $('#motor_speed').val());
    $.get('/motor_speed/'+$('#motor_speed').val());
  });
  $('#motor_position').change(function() {
    console.log('Changed motor position to ' + $('#motor_position').val());
    $.get('/motor_position/'+$('#motor_position').val());
  });

  $('#motor_steps').change(function() {
    console.log('Changed motor steps to ' + $('#motor_steps').val());
    $.get('/motor_steps/'+$('#motor_steps').val());
  });

  $('#motor_direction').change(function() {
    console.log('Changed motor steps to ' + $('#motor_direction').val());
    $.get('/motor_direction/'+$('#motor_direction').val());
  });

  // ============================ STEPPER MOTOR ===============================
  function updateStepperMotor(data) {
    $('#motor_position').text(data['motor']['position']);
    if (data['motor']['state'] === '1') {
      $('#motor_state').toggleClass('label-default', false);
      $('#motor_state').toggleClass('label-success', true);
    } else if (data['motor']['state'] === '0') {
      $('#motor_state').toggleClass('label-default', true);
      $('#motor_state').toggleClass('label-success', false);
    }
  }
  // ============================ STEPPER MOTOR ===============================
```

[PART C](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/PartC.md) Modify main.py for stepper and PWM control code

[LAB7 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab7/setup.md)
