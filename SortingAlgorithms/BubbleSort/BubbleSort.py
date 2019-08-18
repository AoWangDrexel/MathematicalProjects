'''
Author: Ao Wang
Date: 08/06/19 
Description: Bubble sort algorithm
'''

# swaps the elements
def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    
'''
The method sorts the array by looping through each element,
swapping if the number before it is greater than the current
then repeat, but cutting off the end because it is clear
that it is the largest
i.e. 3,1,5,2

first pass
step 1: 3 1 5 2 --> 1 3 5 2
step 2: 1 3 5 2 --> 1 3 5 2
step 3: 1 3 5 2 --> 1 3 2 5

second pass
step 4: 1 3 2 5 --> 1 3 2 5
step 5: 1 3 2 5 --> 1 2 3 5
step 6: 1 2 3 5 --> 1 2 3 5

third pass (continues to check if all elements are sorted)
step 7: 1 2 3 5
step 8: 1 2 3 5
step 9: 1 2 3 5
'''
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j+1] < nums[j]:
                swap(nums,j+1,j)

nums = [5,2,0.5,11,100,-5,99]
bubble_sort(nums)
print(nums)
