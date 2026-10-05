def find_duplicate():
    nums = [1, 3, 4, 2, 3]
    seen = set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
print(find_duplicate())