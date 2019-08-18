
int i = 1;
float [] nums;

void setup() {
  size(640, 320);
  nums = new float[width];
  for (int i = 0; i < width; i++) {
    nums[i] = random(height);
  }
}

void draw() {
  background(0);
  stroke(255);

  for (int i = 0; i< width; i++) {
    line(i, height, i, height - nums[i]);
  }

  if (i < nums.length) {
    int j = i;
    while (j > 0 && nums[j - 1] > nums[j]) {
      swap(nums, j, j - 1);
      j--;
    }
    i++;
  }
}

void swap(float [] nums, int a, int b) {
  float temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
}
