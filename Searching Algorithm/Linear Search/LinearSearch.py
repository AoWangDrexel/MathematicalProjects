def linear_search(nums, find):
    for i in range(len(nums)):
        if(nums[i] == find):
            return i
    return -1

nums = [-1, 0.5, 99, 0, -5, 100]
print(nums)

find = 99
print(str(find) + " can be found at index: " + str(linear_search(nums, find)))
