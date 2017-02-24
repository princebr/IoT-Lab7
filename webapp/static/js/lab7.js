$(document).ready(function() {

  // global arrays needed to buffer data points across events
  var env_table_data = [];

  // the key event receiver function
  iotSource.onmessage = function(e) {
    // must convert all single quoted data with double quote format
    // console.log(e.data);
    var double_quote_formatted_data = e.data.replace(/'/g, '"');
    // now we can parse into JSON
    // console.log(double_quote_formatted_data);
    parsed_json_data = JSON.parse(double_quote_formatted_data);
    console.log(parsed_json_data);
    updateEnvironmentalTableData(parsed_json_data);
    updateStepperMotor(parsed_json_data);
  }

  // Buttons
  $('#motor_start').click(function() {
    console.log('Start Motor Up!');
    $.get('/motor/1');
  });
  // $('#motor_stop').click() ...

  // $('#motor_zero').click() ...

  // $('#motor_multistep').click() ...


  // Text Fields
  $('#motor_speed').change(function() {
    console.log('Changed motor speed to ' + $('#motor_speed').val());
    $.get('/motor_speed/'+$('#motor_speed').val());
  });
  // $('#motor_position').change() ...

  // $('#motor_steps').change() ...

  // $('#motor_direction').change() ...


  // ============================ STEPPER MOTOR ===============================
  function updateStepperMotor(data) {
      // ... add code here ...
  }
  // ============================ STEPPER MOTOR ===============================

  // ============================ DATE FUNCTIONS ==============================
  // previous lab
  function zeropad(num, size) {
      var s = "000000000" + num;
      return s.substr(s.length-size);
  }

  function getDateNow() {
    var d = new Date();
    var date = (d.getFullYear()) + '-' + d.getMonth() + 1 + '-' + d.getDate();
    var time = zeropad(d.getHours(),2) + ':' + zeropad(d.getMinutes(),2) +
    ':' + zeropad(d.getSeconds(),2) + '.' + zeropad(d.getMilliseconds(),3);
    return {time: time, date: (date + " " + time)};
  }
  // ============================ DATE FUNCTIONS ==============================

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
  // ============================== ENV TABLE =================================
  function clearEnvTables() {
    $('tr.env-param-row').each(function(i) {
      $(this).empty();
    });
  }

  // Renders the jQuery-ui elements
  $("#tabs").tabs();

  // ===================================================================
  // RED LED SLIDER
  $( "#slider1" ).slider({
    // ... add code here ...
  });
  $( "#pwm1" ).val( $( "#slider1" ).slider( "value" ) );
  // ... add code to control PWM driver for hardware ...
  // ===================================================================
  // GREEN LED SLIDER
  $( "#slider2" ).slider({
    // ... add code here ...
  });
  $( "#pwm2" ).val( $( "#slider2" ).slider( "value" ) );
  // ... add code to control PWM driver for hardware ...
  // ===================================================================



});
