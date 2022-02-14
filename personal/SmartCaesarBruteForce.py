#Ian Fife
#Caesar Cipher Code Breaker -- brute forces all possible decryptions of an encrypted message

def match_message(message):
    word_list = []
    word_strength = 0

    dictionary = open("dictionary.txt", "r")

    temp = ""
    for char in message.lower():
        if char == " ":
            word_list.append(temp)
            temp = ""
        elif not(char == "!" or char == "?" or char == "."):
            temp += char
    word_list.append(temp)

    for line in dictionary:
        currentWord = line.lower().strip()
        if currentWord in word_list:
            word_strength += 1
    return float(word_strength / len(word_list))

def caesar_breaker():
    #Global symbol set
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    message = input("Enter Encrypted Message: ")
    messages = []
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
        messages.append(translated_message)
    highest_value = 0.0
    highest_word = ""
    message_value = 0.0
    for message in messages:
        message_value = match_message(message)
        if message_value >= highest_value:
            highest_value = message_value
            highest_word = message
    print("The decrypted message is most likely to be \"" + highest_word + "\" with a value of " + str(highest_value))

    if input("Would you like to see the rest of the decryptions? [y] or [n]: ") == "y":
        for message in messages:
            print(message)
    
print("Welcome to the Smart Caesar Cipher Code Breaker Program!")
print("This program will try every possible key to decrypt the message, then attempt to tell you which one is likely to be the true message.")

run = ""

while run != "q":
    caesar_breaker()
    print("----------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("----------------------------------------")

print("Thanks for Using the Program!!")
end = input()
