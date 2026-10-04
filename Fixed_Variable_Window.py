def fixed_window():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3

    window_sum = sum(nums[0:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(fixed_window())