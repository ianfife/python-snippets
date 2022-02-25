#Ian Fife
#This program finds palindromes from a list of words.

def isPalindrome(word):
    if word == word[::-1]:
        return True
    return False

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
