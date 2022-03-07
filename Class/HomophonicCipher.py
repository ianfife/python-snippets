# Ian Fife
# 3/7/2022

# Homophone Cipher
# This program encrypts and decrypts messages using the homophone
# cipher. Symbols are defined with a group of correlating values
# in order to counter frequency analysis.

import random

# Symbol set and corresponding data
char_list = "abcdefghijklmnopqrstuvwxyz"

value_list = [
    ["09", "12", "33", "47", "53", "67", "78" ,"92"],
    ["48", "81"],
    ["13", "41", "62"],
    ["01", "03", "45", "79"],
    ["14", "16", "24", "44", "46", "55", "57", "64", "74", "82", "87", "98"],
    ["10", "31"],
    ["06", "25"],
    ["23", "39", "50", "56", "65", "68"],
    ["32", "70", "73", "83", "88", "93"],
    ["15"],
    ["04"],
    ["26", "37", "51", "84"],
    ["22", "27"],
    ["18", "58", "59", "66", "71", "91"],
    ["00", "05", "07", "54", "72", "90", "99"],
    ["38", "95"],
    ["94"],
    ["29", "35", "40", "42", "77", "80"],
    ["11", "19", "36", "76", "86", "96"],
    ["17", "20", "30", "43", "49", "69", "75", "85", "97"],
    ["08", "61", "63"],
    ["34"],
    ["60", "89"],
    ["28"],
    ["21", "52"],
    ["02"]
]

def homophone_encrypt():
    msg = input("\nEnter Message: ").lower()
    message_encrypt = ""
    
    for char in msg:
        # Supported characters
        if char in char_list:
            # Get the row of the 2d array
            row_val = char_list.index(char)
            # Pick a random value from the row
            hold_var = random.choice(value_list[row_val])
            # Add the random value to the encrypt string
            message_encrypt += hold_var
    
    print("\nOriginal Message: " + msg)
    print("\nEncrypted Message: " + message_encrypt)

def homophone_decrypt():
    msg = input("\nEnter Message: ")
    message_decrypt = ""
    
    # Loop through the message 2 letters at a time
    for i in range(0, len(msg), 2):
        for row in range(len(value_list)):
            # Supported values
            if msg[i:i+2] in value_list[row]:
                # Add corresponding value to the decrypt string
                message_decrypt += char_list[row]
    
    print("\nOriginal Message: " + msg)
    print("\nDecrypted Message: " + message_decrypt)

# Main function -- gets the mode from the user and calls encrypt or decrypt
def homophone_cipher():
    # Get and validate mode
    mode = input("\nEnter [e] for encrypt or [d] for decrypt: ").lower()
    while mode not in ['e', 'd']:
        mode = input("\n --Invalid Input-- Enter [e] for encrypt or [d] for decrypt: ").lower()

    if mode == 'e':
        homophone_encrypt()
    else:
        homophone_decrypt()

## -- Main --

print("Welcome to the Homophone Cipher Program!")

run = ""
while run != "q":
    homophone_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Homophone Cipher Program!")
end = input()
