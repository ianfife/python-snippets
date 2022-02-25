#Ian Fife
#This program converts a list of words to values and then finds the word with the biggest value and prints it out.

def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    #Loops through each letter in the word inputted in the function, converting it to a value based on the letters string.
    #I add 1 each time so that the letters string doesn't have to start with a space (or other character).
    for char in word:
        value += letters.index(char) + 1
    return value

wordList = []
values = []

#Main loop -- tells the user to enter a word or 'Q' to quit. Adds each word added to an array 'wordList'.
main = input("Enter word, 'Q' to quit: ")
while(main != "Q"):
    wordList.append(main)
    main = input("Enter a word: ")

#Loops through the list, calculating the values of each word and appending them onto an array 'values'.
for word in wordList:
    values.append(sum_of_letters(word))

print("\nThe highest value is " + str(max(values)))
print("The word for this value is " + str(wordList[values.index(max(values))]))

end = input()
