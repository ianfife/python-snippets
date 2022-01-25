def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    for char in word:
        value += letters.index(char) + 1
    return value

print(sum_of_letters("hello"))
