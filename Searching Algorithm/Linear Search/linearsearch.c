#include <stdio.h>

int linearSearch(int nums [], int len, int find);
void print(int nums [], int len);

int main(){
    int nums [] = {1, 10, -1, 0, 5, -99, 100, 11, 3};
    int len = sizeof(nums)/sizeof(nums[0]);

    print(nums, len);
    int find = 5;
    printf("%d is at the index, %d \n", find, linearSearch(nums, len, find));
}

int linearSearch(int nums [], int len, int find){
    for(int i = 0; i < len; i++){
        if(nums[i] == find){
            return i;
        }
    }
    return -1;
}

// prints out the array
void print(int nums [], int len){
    for(int i = 0; i < len; i++){
        printf("%d ", nums[i]);
    }
    printf("\n");
}
