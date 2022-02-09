#Ian Fife
#This program finds palindromes from a list of words.
import random

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

words_palindrome = []

#Open dictionary file for reading
dictionary = open('dictionary.txt', 'r')

for line in dictionary:
    #Get each line and strip the newline from the word
    currentWord = line.lower().strip()
    if isPalindrome(currentWord):
        words_palindrome.append(currentWord)
                        

dictionary.close()

print("The palindromes in the dictionary were: " + str(words_palindrome))

end = input()
