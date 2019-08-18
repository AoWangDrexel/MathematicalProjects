/**
 * Author: Ao Wang
 * Date: 08/18/19
 * Description: Insertion Sort Algorithm
 */

#include <stdio.h>

void insertionSort(int nums [], int len);
void swap(int nums [], int a, int b);
void print(int nums [], int len);

int main(){
    int nums [] = { 0, -1, 100, 5, -99, 85, 90, 3 };
    int len = sizeof(nums)/sizeof(nums[0]);
    printf("Unsorted: ");
    print(nums, len);
    printf("Sorted: ");
    insertionSort(nums, len);
    print(nums, len);
}

void insertionSort(int nums [], int len){
    for(int i = 1; i < len; i++){
        int j = i;
        while(j > 0 && nums[j - 1] > nums[j]){
            swap(nums, j - 1, j);
            j--;
        }
    }
}

void swap(int nums [], int a, int b){
    int temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

void print(int nums [], int len){
    printf("[");
    for(int i = 0; i < len - 1; i++){
        printf("%d, ", nums[i]);
    }
    printf("%d]", nums[len - 1]);
    printf("\n");
}
