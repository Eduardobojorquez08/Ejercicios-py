def number_receive(number):
    total = 0
    for digit in str(number):
        total = total + int(digit)
    return total


print(number_receive(1234)) 
print(number_receive(45436)) 
print(number_receive(6364264)) 
print(number_receive(15426262654)) 
print(number_receive(15)) 