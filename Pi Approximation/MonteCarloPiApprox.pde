double inCircle;
double total;
double record;
double approxPi;
double recordPi;
int r;

void setup() {
  size(600, 600);
  inCircle = 0;
  total = 0;
  approxPi = 0;
  recordPi = 0;
  r = 500;
  background(0);
  noFill();
  stroke(255);
  ellipse(width/2, height/2, r, r);
  rect(50, 50, r, r);
}

void draw() {
  for (int i = 0; i < 10000; i++) {
    float randX = random(50, 550);
    float randY = random(50, 550);

    if (Math.sqrt(Math.pow(randX - 300, 2) + Math.pow(randY - 300, 2)) <= 250) {
      inCircle++;
      stroke(#03a9f4);
    } else {
      stroke(#e53935);
    }

    point(randX, randY);
    total++;
  }

  approxPi = 4 * inCircle/total;

  double diff = Math.abs(Math.PI - approxPi);
  double diffRec = Math.abs(PI - recordPi);
  if (diff < diffRec) {
    recordPi = approxPi;
    diffRec = diff;
    println("Record Pi: " + recordPi);
    println("Pi: " + PI);
  }
}
