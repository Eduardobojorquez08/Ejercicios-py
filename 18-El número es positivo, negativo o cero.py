def classify(number):
    if number > 0:
        return "Positive number"
    elif number < 0:
        return "Negative number"
    else:
        return "equal to zero"    

print(classify(1230))
print(classify(-56))
print(classify(0))
    

