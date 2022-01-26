def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    for char in word:
        value += letters.index(char) + 1
    return value

wordList = []
values = []

main = input("Enter word, 'Q' to quit: ")
while(main != "Q"):
    wordList.append(main)
    main = input("Enter a word: ")

for word in wordList:
    values.append(sum_of_letters(word))

print("The highest value is " + str(max(values)))
print("The word for this value is " + str(wordList[values.index(max(values))]))
