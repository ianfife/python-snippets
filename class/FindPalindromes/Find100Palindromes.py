#Ian Fife
#This program finds palindromes from a list of words.

def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    #Loops through each letter in the word inputted in the function, converting it to a value based on the letters string.
    #I add 1 each time so that the letters string doesn't have to start with a space (or other character).
    for char in word:
        value += letters.index(char) + 1
    return value

def isPalindrome(word):
    palindrome = True
    #Test if word is even or odd length to know if we should ignore the middle letter
    if len(word) % 2 == 0:
        #Get the second half of the word
        word_split = word[int(len(word)/2):]
        #Get the first half of the word
        word = word[0:int(len(word)/2)]
        #Reverse the second half of the word
        word_split = word_split[::-1]
        #Test equality
        if word_split != word:
            return False
    else:
        #Get the second half of the word
        word_split = word[int(len(word)/2)+1:]
        #Get the first half of the word
        word = word[0:int(len(word)/2)]
        #Reverse the second half of the word
        word_split = word_split[::-1]
        #Test equality
        if word_split != word:
            return False
    return palindrome

words_palindrome_100 = []

#Open dictionary file for reading
dictionary = open('dictionary.txt', 'r')

for line in dictionary:
    #Get each line and strip the newline from the word
    currentWord = line.lower().strip()
    if isPalindrome(currentWord) and (sum_of_letters(currentWord) == 100):
        words_palindrome_100.append(currentWord)
                        

dictionary.close()

print("The palindromes in the dictionary with a value of 100 were: " + str(words_palindrome_100))

end = input()
