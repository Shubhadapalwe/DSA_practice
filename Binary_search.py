def Binary_Search():
    nums = [2, 4, 7, 10, 13, 18, 21]
    target = 13

    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(Binary_Search())