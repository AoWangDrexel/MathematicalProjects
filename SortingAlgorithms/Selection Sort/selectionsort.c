#include <stdio.h>

// prototyping the methods
void swap(double nums [], int a, int b);
void selectionSort(double nums [], int len);
void print(double nums [], int len);

int main(){
    double nums [] = {1, 10, -1, 0, 5, -99, 100, 10.5, 3};

    // finding length of array
    int len = sizeof(nums) / sizeof(nums[0]);
    selectionSort(nums, len);
    print(nums, len);
}

// The sorting algorithm finds the smallest element in the array
// then swaps it in the first index position, then repeats the process,
// but placing the next smallest in the earlier indexes

// i.e. [-1, 99, 0, 5, 25, 100]
// first: [-1, 99, 0, 5, 25, 100] --> [-1, 99, 0, 5, 25, 100] -1 is the
// smallest, no swap
// second: [-1, 99, 0, 5, 25, 100] --> [-1, 0, 99, 5, 25, 100] swaps 0 to the
// 99's index
// third: [-1, 0, 99, 5, 25, 100] --> [-1, 0, 5, 99, 25, 100]
// fourth: [-1, 0, 5, 99, 25, 100] --> [-1, 0, 5, 25, 99, 100]
// fifth: [-1, 0, 5, 25, 99, 100] -- > [-1, 0, 5, 25, 99, 100]
void selectionSort(double nums [], int len){
    for(int i = 0; i < len - 1; i++){
        int min = i;
        for(int j = i + 1; j < len; j++){
            if(nums[j] < nums[min]){
                min = j;
            }
        }
        swap(nums, min, i);
    }
}

// The method swaps the elements in the array
void swap(double nums [], int a, int b){
    double temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

// prints out the array
void print(double nums [], int len){
    for(int i = 0; i < len; i++){
        printf("%f ", nums[i]);
    }
    printf("\n");
}


