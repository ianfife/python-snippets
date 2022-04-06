# Ian Fife
# 4/6/2022

# Vigenere Cipher V2
# This program encrypts and decrypts messages using the vigenere cipher.
# Messages are encrypted and decrypted using a lookup table.

# By creating the vars here, they are 'global' in the program.
# However, make sure your functions pass information in and out
# using arguments / parameters.

lookupTable = [[]]  # 2-D array for Vigenere Square
tableVar = ""       # a char in the table

keyWord = ""        # the keyword or keyphrase used to encrypt
keyWordList = ""    # keyword REPEATED to length of plainText
keyLetter = ""      # a char in the keyWordList

plainText = ""      # the message string to be encrypted
textLetter = ""     # a char in the message

cipherText = ""     # encrypted text string
cipherLetter = ""   # a char in the cipherText

letterIndex = ""    # contains 'a' ....'z'
letter = ""         # a char in the letterIndex

symbols = 'abcdefghijklmnopqrstuvwxyz'

def createTable():
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(symbols)):
        for char in symbols:
            lookupTable[i].append(char)
        symbols = symbols[1:len(symbols)] + symbols[0]
        lookupTable.append([])

def createKeyWordList(keyWord, plainText):
    keyWordIndex = 0
    keyWordList = ""
    
    for char in plainText:
        if char in symbols:
            keyWordList += keyWord[keyWordIndex % len(keyWord)]
            keyWordIndex += 1
    return keyWordList

def vigenereCipher():
    # Get mode from the user: 
    mode = input("\nChoose [e] encrypt or [d] decrypt: ").lower()

    while mode not in ['e', 'd']:
        mode = input("\nInvalid Input -- Choose [e] encrypt or [d] decrypt: ").lower()

    # Get message from the user:
    plainText = input("\nEnter Message: ").lower()

    # Get key word from the user:
    keyWord = input("\nEnter Key Word: ").lower()

    keyWordList = createKeyWordList(keyWord, plainText)
    
    if mode == 'e':
        print("\nYour encrypted message is: " + encrypt(keyWordList, plainText))
    else:
        print("\nYour decrypted messahe is: " + decrypt(keyWordList, plainText))

def encrypt(keyWordList, plainText):
    cipherText = ""
    keyWordIndex = 0
    
    for char in plainText:
        if char in symbols:
            cipherText += lookupTable[symbols.index(char)][symbols.index(keyWordList[keyWordIndex])]
            keyWordIndex += 1
        else:
            cipherText += char

    return cipherText

def decrypt(keyWordList, cipherText):
    plainText = ""
    keyWordIndex = 0
    
    for char in cipherText:
        if char in symbols:
            textLetter = findRowVal(keyWordList[keyWordIndex])
            keyWordIndex += 1
            plainText += textLetter
        else:
            plainText += char
    return plainText

def findRowVal(keyLetter, textLetter):
    returnLetter
    for char in lookupTable[symbols.index(keyLetter)]:
        if char == textLetter:
            returnLetter = symbols[lookupTable[symbols.index(keyLetter)].index(char)]
    return returnLetter

# -------------------------------------------------------

# Main Program

print("Welcome to the Vigenere Cipher Program!")

createTable()

choice = ''
while choice != 'q':
    vigenereCipher()
    print("---------------------------------------")
    choice = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")
print("\nThanks for using the Vigenere Cipher Program!")
