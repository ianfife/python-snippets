#Ian Fife
#Caesar Cipher Code Breaker -- brute forces all possible decryptions of an encrypted message

def caesar_breaker():
    #Global symbol set
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    message = input("Enter Encrypted Message: ")
    for i in range(1, len(symbols)):
        translated_message = ""
        for char in message:
            #Test if symbols contains the character to see if we can encrypt it
            if char in symbols:
                #Convert the character to a number based on its index in symbols
                index = symbols.index(char)
                #Subtract the shift
                index -= int(i)
                #Wrap around
                while index < 1:
                    index += len(symbols)-1
                #Convert back to a character and append to the new message
                translated_message += symbols[index]
            else:
                translated_message += char
        print(str(i) + ": " + translated_message)

print("Welcome to the Caesar Cipher Code Breaker Program!")
print("This program will try every possible key to decrypt the message.")

run = ""

while run != "q":
    caesar_breaker()
    print("----------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("----------------------------------------")

print("Thanks for Using the Program!!")
end = input()
