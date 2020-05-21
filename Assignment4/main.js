let x = document.getElementById('x');
let y = document.getElementById('y');
let z = document.getElementById('z');
let activity = document.getElementById('activity');
if ( 'Accelerometer' in window ) {
  let sensor = new LinearAccelerationSensor();
  var newMeasurement = {};

  sensor.addEventListener('reading', function(e) {
  x.innerHTML = "x: " + e.target.x;
  y.innerHTML = "y: " + e.target.y;
  z.innerHTML = "z: " + e.target.z;
  
  newMeasurement.x = e.target.x;
  newMeasurement.y = e.target.y;
  newMeasurement.z = e.target.z;

  var message = newMeasurement;
  /* Code to detect movement, uses .7 as threshold for length of Acc vector */
  var accZ = newMeasurement.z;
  var movement = Math.sqrt(Math.pow(newMeasurement.x, 2) + Math.pow(newMeasurement.y, 2) + Math.pow(accZ, 2));
  if(movement>0.7) {
	activity.innerHTML = '<div class=\"alert alert-success text-center\">Walking</div>';
  } else {
	activity.innerHTML = '<div class=\"alert alert-info text-center\">Standing still</div>';
  }
  var msgEdge = JSON.stringify(message);

  //sending data to thingsboard
  const Http = new XMLHttpRequest();
  // Urls where to send the data
  const urlEdge='https://demo.thingsboard.io/api/v1/HrsluvZCQW99jxuqB8Kl/telemetry';
  const urlCloud='https://demo.thingsboard.io/api/v1/6U605oGsbAImxPYCicDB/telemetry'; // Wb6jsCSm5TKljCke0sjC
  
  Http.open("POST",urlEdge);
  Http.send(msgEdge);

  var msgCloud = '{\"sensor\":\"true\",\"x\":\"' + message.x + '\",\"y\":\"' + message.y + '\",\"z\":\"' + message.z + '\"}';
  Http.open("POST",urlCloud);
  Http.send(msgCloud);

  setInterval( function() {}, 1000);
  });
  sensor.start();
}
else y.innerHTML = 'Accelerometer not supported';