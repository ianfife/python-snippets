# Cryptography

# Author: Ian Fife
# Spring 2022

# This program modifies the standard encryption/decryption program
# by adding an additional "password phrase" to the symbol set.
# Each character in the phrase (no repeats) is appended at the LEFT side
# of the symbol list, and the corresponding characters are removed from
# their normal location in the symbol set. In this way, the ORDER of the
# symbol set is unique based on the pass phrase.

# This new feature creates an additional layer of security, since
# encoding/decoding a message will require BOTH a key and a pass phrase.

def shiftCipher():

    # Helper function for appending pass phrase to symbol set
    def adjustSymbols(symbols, passPhrase):
        
        # First - copy the pass phrase to remove spaces and repeats
        new_passphrase = ""
        for char in passPhrase:
            if char != " " and not char in new_passphrase:
                new_passphrase += char
        
        # Second - remove all the matching characters from the symbol set
        new_symbols = ""
        for char in symbols:
            if not char in new_passphrase:
                new_symbols += char
        symbols = new_symbols
        
        # Third - concatenate modified pass phrase to the left of symbols
        symbols = new_passphrase + symbols

        print(symbols)
        return symbols
        # end of helper function
        
    # Create an empty string to hold translated text
    translated = ""

    # Create the symbol set
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
    
    # Get mode from the user: 
    mode = input("\nChoose [e] encrypt or [d] decrypt: ")

    # Get message from the user:
    message = input("\nEnter Message: ")

    # Get shift key from the user:
    shift = int(input("\nSelect shift key: "))

    # NEW! Get pass phrase from the user:
    passPhrase = input("\nEnter Pass Phrase: ")

    # NEW! Adjust the symbol set using the pass phrase
    symbols = adjustSymbols(symbols, passPhrase)

    # Process each character and append to translated text
    for ch in message:
        if ch in symbols:
            pos = symbols.index(ch) # find the index value in symbols
            if mode == 'e':         
                pos += shift  # Add the shift key to encrypt
                if pos >= len(symbols): # Adjust for wrapping
                    pos -= len(symbols)
                    
            if mode == 'd':         
                pos -= shift  # Subtract the shift key to decrypt
                if pos < 0:             # Adjust for wrapping
                    pos += len(symbols)

            translated += symbols[pos]

        else:
            translated += ch  # Any chars not in symbols are
                              # appended WITHOUT shifting,
                              # including SPACES.
                              
    print("\nOriginal Message: " + message)
    print("\nTranslated Message: " + str(translated))           
# -------------------------------------------------------

# Main Program

print("Welcome to the Caesar Cipher Encryption Program!")

choice = ''
while choice != 'q':
    shiftCipher()
    print(" \n---------------------------------------")
    choice = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")
print("\nThanks for using the Caesar Cipher Encryption Program!")
end = input() # This keeps the black screen visible when using exe
