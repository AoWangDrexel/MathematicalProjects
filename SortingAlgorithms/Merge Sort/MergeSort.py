"""
Author: Ao Wang
Date: 08/20/19
Description: Merge Sort Algorithm
"""

def merge(left, right):
    result = []
    leftInd = 0
    rightInd = 0
    resultInd = 0
    
    while leftInd < len(left) or rightInd < len(right):
        if leftInd < len(left) and rightInd < len(right):
            if left[leftInd] < right[rightInd]:
                result.append(left[leftInd])
                leftInd += 1
            else:
                result.append(right[rightInd])
                rightInd += 1
        elif leftInd < len(left):
            result.append(left[leftInd])
            leftInd += 1
        elif rightInd < len(right):
            result.append(right[rightInd])
            rightInd += 1
    
    return result

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = []
    right = []
    
    for i in range(mid):
        left.append(nums[i])
    for i in range(mid, len(nums)):
        right.append(nums[i])
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)

nums = [0, -1, 100, 5, -99, 85, 90, 3]
print("Unsorted: " + str(nums))
print("Sorted: " + str(mergeSort(nums)))
