/*
Author: Ao Wang
Date: 08/07/19
Description: Simple animation of bubble sort

*/
var nums = []
var i;
var j;
var k;

function setup() {
  createCanvas(400, 400);
  i = 0;
  j = 0;
  k = 0;
  
  // stores random values into the array from 0 to height
  for(var i = 0; i < width; i++){
    nums[i] = random(height);
  }
}

function draw() {
  background(0);
  stroke(255);
  
  // draws the lines
  for(var i = 0; i < width; i++){
    line(i, height, i, height - nums[i]);
  }
  
  // the sorting algorithm
  if(k < width){
    for(var j = 0; j < width - k - 1; j++){
      if(nums[j + 1] < nums[j]){
        swap(nums, j + 1, j);
      }
    }
  }
  k++;
}

// The method swaps the elements in the array
swap = function(nums, a, b){
  var temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}


