var z = 1;
var nums = [];

function setup() {
  createCanvas(400, 400);
  
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
  
  if(z < width){
    var j = z;
    while(j > 0 && nums[j - 1] > nums[j]){
      swap(nums, j - 1, j);
      j--;
    }
    z++;
  }
}


swap = function(nums, a, b){
  var temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}
