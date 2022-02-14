#Ian Fife
#Caesar Cipher Code Breaker -- brute forces all possible decryptions of an encrypted message

def caesar_breaker():
    #Global symbol set
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def match_message(message):
        word_list = []
        word_strength = 0

        dictionary = open("largeDictionary.txt", "r")

        temp_message = message.lower().replace("! ", " ").replace("? ", " ").replace(". ", " ")

        bad_chars = []
        for char in temp_message:
            if char not in symbols:
                temp_message = temp_message.replace(char, "")

        if temp_message[-1] == "!" or temp_message[-1] == "?" or temp_message[-1] == ".":
            temp_message = temp_message[0:len(temp_message)-1]
        word_list = temp_message.split(" ")
        
        for line in dictionary:
            currentWord = line.lower().strip()
            if currentWord in word_list:
                word_strength += word_list.count(currentWord)
        
        return float(word_strength / len(word_list))

    message = input("Enter Encrypted Message: ")
    messages = []
    for i in range(0, len(symbols)):
        translated_message = ""
        for char in message:
            #Test if symbols contains the character to see if we can encrypt it
            if char in symbols:
                #Convert the character to a number based on its index in symbols
                index = symbols.index(char)
                #Subtract the shift
                index -= int(i)
                #Wrap around
                while index < 0:
                    index += len(symbols)
                #Convert back to a character and append to the new message
                translated_message += symbols[index]
            else:
                translated_message += char
        messages.append(translated_message)
    highest_value = 0.0
    highest_word = ""
    message_value = 0.0
    ordered_messages = []
    ordered_values = []
    for message in messages:
        message_value = match_message(message)
        ordered_messages.append(message)
        ordered_values.append(message_value)
        if message_value >= highest_value:
            highest_value = message_value
            highest_word = message
    print("The decrypted message is most likely to be \"" + highest_word + "\" with a value of " + str(round(highest_value, 4)))

    if input("Would you like to see the rest of the decryptions? [y] or [n]: ") == "y":
        zipped = sorted(zip(ordered_values, ordered_messages))
        for value, message in zipped:
            print(message, round(value, 4))
    
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
