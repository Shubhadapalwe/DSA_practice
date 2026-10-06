def second_largest():
    nums = [10, 5, 20, 8, 15]

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


print(second_largest())