/**
 *
 * @author aowang
 * Date: 08/06/19
 * Description: Simple bubble sort algorithm
 *
 */

#include <stdio.h>

// prototyping the methods
void bubbleSort(double nums [], int len);
void swap(double nums[], int a, int b);
void print(double nums [], int len);

int main(){
    double nums [] = {0, -1, 100, 2, 3, -99, 1.5, 99.5};

    // C does not have a build in length or len like Python or Java, but can find it using sizeof method
    // that is also why the parameters include len
    int len = sizeof(nums)/sizeof(nums[0]);
    bubbleSort(nums, len);
    print(nums,len);
}

// The method sorts the array by looping through each element,
// swapping if the number before it is greater than the current
// then repeat, but cutting off the end because it is clear
// that it is the largest
// i.e. 3,1,5,2

// first pass
// step 1: 3 1 5 2 --> 1 3 5 2
// step 2: 1 3 5 2 --> 1 3 5 2
// step 3: 1 3 5 2 --> 1 3 2 5

// second pass
// step 4: 1 3 2 5 --> 1 3 2 5
// step 5: 1 3 2 5 --> 1 2 3 5
// step 6: 1 2 3 5 --> 1 2 3 5

// third pass (continues to check if all elements are sorted)
// step 7: 1 2 3 5
// step 8: 1 2 3 5
// step 9: 1 2 3 5

void bubbleSort(double nums [], int len){
    for(int i = 0; i < len; i++){
        for(int j = 0; j < len - i - 1; j++){
            if(nums[j+1] < nums[j]){
                swap(nums, j+1, j);
            }
        }
    }
}

// swapping the elements
void swap(double nums [], int a, int b){
    double temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

// printing the array
void print(double nums [], int len){
    for(int i = 0; i < len; i++){
        printf("%f ", nums[i]);
    }
    printf("\n");
}
