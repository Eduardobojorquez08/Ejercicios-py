# write a function thath receives a number and returns if it is even or odd

def number_check(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(number_check(4))
print(number_check(7))
print(number_check(98))
print(number_check(35))
print(number_check(67))
print(number_check(65))