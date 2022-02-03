#Ian Fife
#This program converts a list of words to values and then finds all the words that have a value of 100.

def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    #Loops through each letter in the word inputted in the function, converting it to a value based on the letters string.
    #I add 1 each time so that the letters string doesn't have to start with a space (or other character).
    for char in word:
        value += letters.index(char) + 1
    return value

words_100 = []

#Open dictionary file for reading
dictionary = open('dictionary.txt', 'r')

for line in dictionary:
    #Get each line and strip the newline from the word
    currentWord = line.lower().strip()
    if sum_of_letters(currentWord) == 100:
        #Append to the list if the word has a value of 100
        words_100.append(currentWord)

dictionary.close()

print("The words with a value of 100 are: " + str(words_100))

end = input()
