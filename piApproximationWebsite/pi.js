function circle() {
  var canvas = document.getElementById("can");
  var ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.arc(canvas.width / 2, canvas.height / 2, 250, 0, 2 * Math.PI);
  ctx.stroke();
}

function simulate() {
  var canvas = document.getElementById("can");
  var ctx = canvas.getContext("2d");
  for (var i = 0; i < 100; i++) {
    var randX = Math.random() * 500;
    var randY = Math.random() * 500;
    var r =
      Math.sqrt(Math.pow(randX - 250, 2) + Math.pow(randY - 250, 2)) <= 250;
    if (r) {
      ctx.beginPath();
      ctx.strokeStyle = "green";
      ctx.rect(randX, randY, 0.5, 0.5);
      ctx.stroke();
    } else {
      ctx.beginPath();
      ctx.strokeStyle = "red";
      ctx.rect(randX, randY, 0.5, 0.5);
      ctx.stroke();
    }
  }
}

function calculatePi() {
  var inCircle = 0;
  var total = 0;

  // circle x^2 + y^2 = r^2
  // square is 1 by 1
  // circle radius = 1/2

  var recordAccurate = 0;

  while (true) {
    var randX = Math.random() - 0.5;
    var randY = Math.random() - 0.5;

    // random x and y coordinates, -0.5<= x < 0.5, -0.5 <= y < 0.5
    var r = Math.sqrt(Math.pow(randX, 2) + Math.pow(randY, 2)) <= 0.5;
    if (r) {
      inCircle++;
    }
    total++;

    // caluation of 4 * pi/4
    var currentPi = 4 * inCircle / total;

    var functionPi = Math.PI;
    var recordDiff = Math.abs(recordAccurate - functionPi);

    var diff = Math.abs(currentPi - functionPi);

    // finding smallest difference of approximation and java's math library of pi
    if (diff < recordDiff) {
      recordAccurate = currentPi;
      var cont = confirm("Would you like an approximation of pi?");
      if (cont) {
        alert("Record Pi: " + recordAccurate);
      } else {
        break;
      }
    }
  }
}

