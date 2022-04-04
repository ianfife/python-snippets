# Ian Fife
# 4/4/2022

# Vigenere Cipher V1
# This program encrypts and decrypts messages using the vigenere cipher.
# Messages are encrypted using a mulltitude of variations on the
# shift cipher depending on a key word.

def vigenere_cipher():

    # Create an empty string to hold translated text
    translated = ""

    # Create the symbol set
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    
    #Get mode from the user: 
    mode = input("\nChoose [e] encrypt or [d] decrypt: ").lower()

    while mode not in ['e', 'd']:
        mode = input("\nInvalid Input -- Choose [e] encrypt or [d] decrypt: ").lower()

    #Get message from the user:
    message = input("\nEnter Message: ")

    # Get key word from the user:
    key_word = input("\nEnter Key Word: ")

    # Process each character and append to translated text
    key_word_index = 0
    for ch in message:
        if ch in symbols:
            pos = symbols.index(ch) # find the index value in symbols
            if mode == 'e':
                pos += symbols.index(key_word[key_word_index % len(key_word)])    # Add the key word to encrypt
                while pos >= len(symbols):  # Adjust for wrapping
                    pos -= len(symbols)
                    
            if mode == 'd':
                pos -= symbols.index(key_word[key_word_index % len(key_word)])  # Subtract the key word to decrypt
                while pos < 0:  # Adjust for wrapping
                    pos += len(symbols)

            translated += symbols[pos]
            key_word_index += 1
        else:
            translated += ch  # Any chars not in symbols are
                              # appended WITHOUT shifting,
                              # including SPACES.
                              
    print("\nOriginal Message: " + message)
    print("\nTranslated Message: " + str(translated))           
# -------------------------------------------------------

# Main Program

print("Welcome to the Vigenere Cipher Program!")

choice = ''
while choice != 'q':
    vigenere_cipher()
    print("\n---------------------------------------")
    choice = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Vigenere Cipher Program!")
end = input() # This keeps the black screen visible when using exe
