word = "banana"

def coun_letters(word):
    letters = {}
    for letter in word:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters 
print(coun_letters(word))



         

       