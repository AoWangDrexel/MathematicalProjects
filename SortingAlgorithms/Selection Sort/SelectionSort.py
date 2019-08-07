'''
Author: Ao Wang
Date: 08/07/19 
Description: Simple selection sort algorithm
'''

# The function swaps two numbers in the list
def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    
# The sorting algorithm finds the smallest element in the array
# then swaps it in the first index position, then repeats the process,
# but placing the next smallest in the earlier indexes

# i.e. [-1, 99, 0, 5, 25, 100]
# first: [-1, 99, 0, 5, 25, 100] --> [-1, 99, 0, 5, 25, 100] -1 is the
# smallest, no swap
# second: [-1, 99, 0, 5, 25, 100] --> [-1, 0, 99, 5, 25, 100] swaps 0 to the
# 99's index
# third: [-1, 0, 99, 5, 25, 100] --> [-1, 0, 5, 99, 25, 100]
# fourth: [-1, 0, 5, 99, 25, 100] --> [-1, 0, 5, 25, 99, 100]
# fifth: [-1, 0, 5, 25, 99, 100] -- > [-1, 0, 5, 25, 99, 100]
def selection_sort(nums):
    for i in range(len(nums) - 1):
        min_i = i
        for j in range(i + 1, len(nums)):
            if(nums[j] < nums[min_i]):
                min_i = j
        swap(nums,i,min_i)
        
nums = [5,2,0.5,11,100,-5,99]
selection_sort(nums)
print(nums)
