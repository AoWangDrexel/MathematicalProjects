def binary_search(nums, find):
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = (low + high) // 2
        if nums[mid] < find:
            low = mid + 1
        elif nums[mid] == find:
            return mid
        else:
            high = mid - 1
    return -1
    
nums = [-1, 0.5, 99, 0, -5, 100]
print(nums)

nums = sorted(nums)
print(nums)

find = 99
print(str(find) + " can be found at index: " + str(binary_search(nums, find)))
