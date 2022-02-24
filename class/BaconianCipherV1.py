# Ian Fife
# 2/22/2022

# Baconian Cipher V1
# This Program encrypts and decrypts messages
# using the Baconian Cipher. It substitutes letters
# with a string of five binary digits.

def baconian_cipher():
    # Symbol set
    symbols = {
        "A" : "aaaaa", "B" : "aaaab", "C" : "aaaba", "D" : "aaabb",
        "E" : "aabaa", "F" : "aabab", "G" : "aabba", "H" : "aabbb",
        "I" : "abaaa", "J" : "abaab", "K" : "ababa", "L" : "ababb",
        "M" : "abbaa", "N" : "abbab", "O" : "abbba", "P" : "abbbb",
        "Q" : "baaaa", "R" : "baaab", "S" : "baaba", "T" : "baabb",
        "U" : "babaa", "V" : "babab", "W" : "babba", "X" : "babbb",
        "Y" : "bbaaa", "Z" : "bbaab"
    }

    message = input("\nEnter Message: ")
    mode = ""

    while mode != "e" and mode != "d":
        mode = input("\nChoose [e] encrypt or [d] decrypt: ")

        # Encrypt
        if mode == "e":
            encryption_message = input("\nEnter Encryption Message: ")
            min_length = 0

            # Get the minimum length by testing for supported characters
            # and adding 5 for each one.
            for char in message:
                if char.upper() in symbols.keys():
                    min_length += 5

            # Verify that the "outer message" is long enough.
            encryption_message_length = 0
            for char in encryption_message:
                if char.upper() in symbols.keys():
                    encryption_message_length += 1
                    
            # Error handling if the length is not enough.
            while encryption_message_length < min_length:
                encryption_message_length = 0
                print("\nYour encryption message must be at least " + str(min_length) + " characters long. Try again.")
                encryption_message = ""
                encryption_message = input("\nEnter Encryption Message (or press enter to use default option): ")
                
                # Default option
                if encryption_message == "":
                    while encryption_message_length < min_length:
                        encryption_message += "stock "
                        encryption_message_length += 5
                
                else:
                    # Calculate length again
                    for char in encryption_message:
                        if char.upper() in symbols.keys():
                            encryption_message_length += 1

            new_message = ""
            for char in message:
                # Convert each character into a value using the dictionary
                if char.upper() in symbols.keys():
                    new_message += symbols[char.upper()]
            
            new_encryption_message = ""
            i = 0
            for char in new_message:
                # Account for unsupported characters
                while encryption_message[i].upper() not in symbols.keys():
                    new_encryption_message += encryption_message[i]
                    i += 1
                # Make the character in the new message uppercase if the
                # parallel value is an A, and make it lowercase for B
                if char == "a":
                    new_encryption_message += encryption_message[i].upper()
                else:
                    new_encryption_message += encryption_message[i].lower()
                i += 1
            
            # Print out results
            print("\nOriginal Message: " + message)
            print("Encryption Key: " + new_message)
            print("Original Encrypt Message: " + encryption_message)
            print("Encrypted Message: " + new_encryption_message)

        # Decrypt
        elif mode == "d":
            new_message = ""
            new_key = ""

            for char in message:
                # Account for unsupported characters
                if char.upper() not in symbols.keys():
                    pass
                # Add a b for lowercase letters
                elif char.islower():
                    new_key += "b"
                # Add an a for uppercase letters
                else:
                    new_key += "a"

            # Loop through the new key in increments of 5, extracting
            # 5 characters at a time, and converting those back into
            # characters by reversing the original dictionary.
            for i in range(5, len(new_key)+5, 5):
                if len(new_key[i-5:i]) < 5:
                    break
                new_message += dict(map(reversed, symbols.items()))[new_key[i-5:i]]

            # Print out results
            print("\nOriginal Message: " + message)
            print("Decryption Key: " + new_key)
            print("Decrypted Message: " + new_message)
        else:
            print("\nIncorrect value. You must enter [e] or [d].")

# -- Main --

print("Welcome to the Baconian Cipher Program!")
print("\nYour 'inner' message will be hidden in an 'outer' message that is at least 5 times longer than the inner.")

run = ""
while run != "q":
    baconian_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Baconian Cipher Program!")
end = input()
