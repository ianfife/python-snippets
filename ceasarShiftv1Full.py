def ceasar_encrypt():
    message_lowercase = message.lower()
    shiftedChars = ""
    
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
    
    for char in message_lowercase:
        ordChar = ord(char)
        ordChar -= shift
        while ordChar < 97:
            ordChar += 26
        ordChar = chr(ordChar)
        shiftedChars += ordChar

    return shiftedChars

choice = input("Do you want to encrypt or decrypt? Type \"Encrypt\" to encrypt and \"Decrypt\" to decrypt.\n")
while choice.lower() != "encrypt" or "decrypt":
    if choice.lower() == "encrypt":
        message = input("Enter text: ")
        shift = int(input("Enter shift: "))
        shiftedChars = ceasar_encrypt()
    elif choice.lower == "decrypt":
        message = input("Enter text: ")
        shift = int(input("Enter shift: "))
        shiftedChars = ceasar_decrypt()
    else:
        print("Incorrect value. You must enter Encrypt or Decrypt.")
        choice = input("Do you want to encrypt or decrypt? Type \"Encrypt\" to encrypt and \"Decrypt\" to decrypt.\n")
    
print(message)
print(shiftedChars)

end = input()
