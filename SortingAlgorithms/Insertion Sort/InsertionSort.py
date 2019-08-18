"""
Author: Ao Wang
Date: 08/18/19
Description: Insertion Sort Algorithm
"""

def swap(nums, a, b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp

def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            swap(nums, j - 1, j)
            j -= 1
    return nums

nums = [0, -1, 100, 5, -99, 85, 90, 3]
print("Unsorted: " + str(nums))
insertion_sort(nums)
print("Sorted: " + str(insertion_sort(nums)))
