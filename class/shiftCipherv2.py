#Ian Fife
#This program encrypts and decrypts a large array of symbols.

def shift_cipherv2():
    symbols = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?."
    run = ""
    print("Welcome to the Caesar Cipher Encryption Program!\n")
    while(run != 'q'):
        mode = input("Choose [e] encrypt or [d] decrypt: ")
        if mode == 'e':
            message = input("\nEnter Message: ")
            shift = input("\nSelect Shift Key: ")
            translated_message = ""
            for char in message:
                #Test if symbols contains the character to see if we can encrypt it
                if char in symbols:
                    #Convert the character to a number based on its index in symbols
                    index = symbols.index(char)
                    #Add the shift
                    index += int(shift)
                    #Wrap around
                    while index > len(symbols):
                        index -= len(symbols)
                    #Convert back to a character and append to the new message
                    translated_message += symbols[index]
                else:
                    translated_message += char
            print("\nOriginal Message: " + message)
            print("\nTranslated Message: " + translated_message)
        elif mode == 'd':
            message = input("\nEnter Message: ")
            shift = input("\nSelect Shift Key: ")
            translated_message = ""
            for char in message:
                #Test if symbols contains the character to see if we can encrypt it
                if char in symbols:
                    #Convert the character to a number based on its index in symbols
                    index = symbols.index(char)
                    #Subtract the shift
                    index -= int(shift)
                    #Wrap around
                    while index < 1:
                        index += len(symbols)
                    #Convert back to a character and append to the new message
                    translated_message += symbols[index]
                else:
                    translated_message += char
            print("\nOriginal Message: " + message)
            print("\nTranslated Message: " + translated_message)
        else:
            print("Incorrect value. You must enter [e] or [d]")
        print("\n-------------------------------------")
        run = input("Press ENTER to continue, 'q' to quit: ")
        print("-------------------------------------\n")

shift_cipherv2()
