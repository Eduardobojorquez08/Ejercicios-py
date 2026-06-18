def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(find_largest([3, 1, 7, 2]))    
print(find_largest([10, 55, 3, 99])) 
print(find_largest([4, 4, 4]))