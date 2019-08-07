var nums = []
var i;
var j;
var k;

function setup() {
  createCanvas(400, 400);
  i = 0;
  j = 0;
  k = 0;
  for(var i = 0; i < width; i++){
    nums[i] = random(height);
  }
}

function draw() {
  background(0);
  stroke(255);
  for(var i = 0; i < width; i++){
    line(i, height, i, height - nums[i]);
  }
  
  
  if(k < width - 1){
    var min = k;
    for(var j = k + 1; j < width; j++){
      if(nums[j] < nums[min]){
        min = j;
      }
    }
    swap(nums, min, k);
  }
  k++;
}

swap = function(nums, a, b){
  var temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}


