# Ian Fife
# 2/22/2022

# Baconian Cipher V1
# This Program encrypts and decrypts messages
# using the Baconian Cipher. It substitutes letters
# with a string of five binary digits.

def baconian_cipher():
    # Symbol set
    symbols = {
        "A" : "AAAAA", "B" : "AAAAB", "C" : "AAABA", "D" : "AAABB",
        "E" : "AABAA", "F" : "AABAB", "G" : "AABBA", "H" : "AABBB",
        "I" : "ABAAA", "K" : "ABAAB", "L" : "ABABA", "M" : "ABABB",
        "N" : "ABBAA", "O" : "ABBAB", "P" : "ABBBA", "Q" : "ABBBB",
        "R" : "BAAAA", "S" : "BAAAB", "T" : "BAABA", "U" : "BAABB",
        "W" : "BABAA", "X" : "BABAB", "Y" : "BABBA", "Z" : "BABBB"
    }

    message = input("\nEnter Message: ")
    mode = ""
    while mode != "e" and mode != "d":
        mode = input("\nChoose [e] encrypt or [d] decrypt: ")
        # Encrypt
        if mode == "e":
            encryption_message = input("\nEnter Encryption Message: ")
            while len(encryption_message) < len(message) * 5:
                print("\nYour encryption message must be at least " + str(len(message)*5) + " characters long. Try again.")
                encryption_message = input("\nEnter Encryption Message: ")
            new_message = ""
            for char in message:
                # Convert each character into a value using the dictionary
                new_message += symbols[char]
            
            new_encryption_message = ""
            i = 0
            for char in new_message:
                # Account for spaces
                while encryption_message[i] == " ":
                    new_encryption_message += " "
                    i += 1
                # Make the character in the new message lowercase if the
                # parallel value is an A, and make it uppercase for B
                if char == "A":
                    new_encryption_message += encryption_message[i].lower()
                else:
                    new_encryption_message += encryption_message[i].upper()
                i += 1
            
            print("\nOriginal Message: " + message)
            print("Encryption Key: " + new_message)
            print("Original Encrypt Message: " + encryption_message)
            print("Encrypted Message: " + new_encryption_message)
        # Decrypt
        elif mode == "d":
            new_message = ""
            new_key = ""
            for char in message:
                # Account for spaces
                if char == " ":
                    pass
                # Add an A for lowercase letters
                elif char.islower():
                    new_key += "A"
                # Add a B for upercase letters
                else:
                    new_key += "B"
            # Loop through the new key in increments of 5, extracting
            # 5 characters at a time, and converting those back into
            # characters by reversing the original dictionary.
            for i in range(5, len(new_key)+5, 5):
                new_message += dict(map(reversed, symbols.items()))[new_key[i-5:i]]

            print("\nOriginal Message: " + message)
            print("Decryption Key: " + new_key)
            print("Decrypted Message: " + new_message)
        else:
            print("\nIncorrect value. You must enter [e] or [d].")

# -- Main --

print("Welcome to the Baconian Cipher Program!")
run = ""

while run != "q":
    baconian_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Baconian Cipher Program!")
end = input()
