#Ian Fife
#This program creates a scenario where the user chooses between decrypting and encrypting and inputs a word to be either encrypted or decrypted.
#Both the encrypt and decrypt methods are defined on their own function and are called in the main loop depending on user input.

def ceasar_encrypt():
    message_lowercase = message.lower()
    shiftedChars = ""

    #Loops through each letter in the word, converting each to a number with the ord() function,
    #then adding the shift, substracting 26 while it is above the value 122 (which represents the letter 'z')
    #to loop back around to the front of the alphabet. Then converts back to a character and appends it to the returned string.
    for char in message_lowercase:
        ordChar = ord(char)
        ordChar += shift
        while ordChar > 122:
            ordChar -= 26
        ordChar = chr(ordChar)
        shiftedChars += ordChar

    return shiftedChars

def ceasar_decrypt():
    message_lowercase = message.lower()
    shiftedChars = ""

    #Loops through each letter in the word, converting each to a number just like the encrypt function.
    #Substracts the shift instead of adding it in order to reverse the encryption. Then loops back around by adding
    #26 if it is less than 97 (which represents the letter 'a'). Then it converts back to a character and appends it to a returned string.
    for char in message_lowercase:
        ordChar = ord(char)
        ordChar -= shift
        while ordChar < 97:
            ordChar += 26
        ordChar = chr(ordChar)
        shiftedChars += ordChar

    return shiftedChars

choice = input("Do you want to encrypt or decrypt? Type \"Encrypt\" to encrypt and \"Decrypt\" to decrypt.\n")
#Main loop -- checks user input. If it matches encrypt or decrypt, the respective function takes place.
#If it isn't either of the two words, it loops back around and forces the user to choose again.
while choice.lower() != "encrypt" or "decrypt":
    if choice.lower() == "encrypt":
        message = input("\nEnter text: ")
        shift = int(input("Enter shift: "))
        shiftedChars = ceasar_encrypt()
        break
    elif choice.lower() == "decrypt":
        message = input("\nEnter text: ")
        shift = int(input("Enter shift: "))
        shiftedChars = ceasar_decrypt()
        break
    else:
        print("\nIncorrect value. You must enter Encrypt or Decrypt.")
        choice = input("Do you want to encrypt or decrypt? Type \"Encrypt\" to encrypt and \"Decrypt\" to decrypt.\n")
    
print("The original messages was: " + message)
print("The new messages is: " + shiftedChars)

end = input()
