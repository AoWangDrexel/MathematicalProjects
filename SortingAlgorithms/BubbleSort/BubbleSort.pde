/*
Author: Ao Wang
Date: 08/07/19
Description: Simple animation of bubble sort
*/

float [] nums;
int i;
int j;

void setup() {
  size(640, 320);
  i = 0;
  j = 0;
  
  // create array the width of the screen
  nums = new float[width];
  
  // stores in random values from 0 to height in nums
  for (int i = 0; i < nums.length; i++) {
    nums[i] = random(height);
  }
}

void draw() {
  background(0);
  stroke(255);
  
  // draws the lines
  for (int i = 0; i < nums.length; i++) {
    line(i, height, i, height - nums[i]);
  }
  
  // the sorting algoritm
  if (i < nums.length) {
    for (int j = 0; j < nums.length - i - 1; j++) {
      if (nums[j+1] < nums[j]) {
        swap(nums, j + 1, j);
      }
    }
  }
  i++;
}

// The method for swapping
void swap(float [] nums, int a, int b) {
  float temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}
