#include <stdio.h>

int binarySearch(int nums [], int high, int find);
void swap(int nums [], int a, int b);
void selectionSort(int nums [], int len);
void print(int nums [], int len);

int main(){
    int nums [] = {1, 10, -1, 0, 5, -99, 100, 11, 3};
    int len = sizeof(nums)/sizeof(nums[0]);
    
    printf("Unsorted: ");
    print(nums, len);
    
    selectionSort(nums, len);
    printf("Sorted: ");
    print(nums, len);
    
    printf("\n");
    int find = 5;
    printf("%d is at the index, %d \n", find, binarySearch(nums, len, find));
}

// The method finds the wanted element and returns the index
// using a binary search
int binarySearch(int nums [], int high, int find){
    int low = 0;
    while(low <= high){
        int mid = (low + high)/2;
        if(nums[mid] < find){
            low = mid + 1;
        }else if(nums[mid] == find){
            return mid;
        }else{
            high = mid - 1;
        }
    }
    return -1;
}

// The method does a simple selection sort
void selectionSort(int nums [], int len){
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
void swap(int nums [], int a, int b){
    double temp = nums[a];
    nums[a] = nums[b];
    nums[b] = temp;
}

// prints out the array
void print(int nums [], int len){
    for(int i = 0; i < len; i++){
        printf("%d ", nums[i]);
    }
    printf("\n");
}
