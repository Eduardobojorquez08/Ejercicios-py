numbers = [4, 5, 8, 9, 3, 1, 6, 7, 2]

def get_greater(nums, n):
    result = []
    for num in nums:
        if num > n:
            result.append(num)
    return result

print(get_greater(numbers, 4))