float [] nums;
int i;
int j;

void setup() {
  size(640, 320);
  i = 0;
  j = 0;
  nums = new float[width];
  
  for (int i = 0; i < nums.length; i++) {
    nums[i] = random(height);
  }
}

void draw() {
  background(0);
  stroke(255);
  
  for (int i = 0; i < nums.length; i++) {
    line(i, height, i, height - nums[i]);
  }
  
  if (i < nums.length - 1) {
    int min = i;
    for (int j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[min]) {
        min = j;
      }
    }
    swap(nums, min, i);
  }
  i++;
}

void swap(float [] nums, int a, int b) {
  float temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}
