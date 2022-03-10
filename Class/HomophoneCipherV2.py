# Ian Fife
# 3/7/2022

# Homophone Cipher V2
# This program encrypts and decrypts messages using the homophone
# cipher. Symbols are defined with a group of correlating values
# in order to counter frequency analysis. In V2, the key is randomly
# generated each time.

import random

# Symbol set and corresponding data
symbols = "abcdefghijklmnopqrstuvwxyz "

keys = [[8], [2], [3], [4], [11], [2], [2], [6], [6],
              [1], [1], [4], [2], [6], [7], [2], [1], [6],
              [6], [9], [3], [1], [2], [1], [2], [1], [1]]

# All possible values
val_list = ["00", "01", "02", "03", "04", "05",
            "06", "07", "08", "09", "10", "11",
            "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23",
            "24", "25", "26", "27", "28", "29",
            "30", "31", "32", "33", "34", "35",
            "36", "37", "38", "39", "40", "41",
            "42", "43", "44", "45", "46", "47",
            "48", "49", "50", "51", "52", "53",
            "54", "55", "56", "57", "58", "59",
            "60", "61", "62", "63", "64", "65",
            "66", "67", "68", "69", "70", "71",
            "72", "73", "74", "75", "76", "77",
            "78", "79", "80", "81", "82", "83",
            "84", "85", "86", "87", "88", "89",
            "90", "91", "92", "93", "94", "95",
            "96", "97", "98", "99"]

def create_keys():
    # Loop through each row
    for row in keys:
        # Grab the bin size stored in the keys 2d array
        bin_size = row.pop(0)
        for i in range(bin_size):
            # Append a randomly chosen value from the val_list
            # and remove that value from val_list, so there
            # aren't any repeats.
            row.append(val_list.pop(val_list.index(random.choice(val_list))))

def homophone_encrypt():
    msg = input("\nEnter Message: ").lower()
    message_encrypt = ""
    
    for char in msg:
        # Supported characters
        if char in symbols:
            # Get the row of the 2d array
            row_val = symbols.index(char)
            # Pick a random value from the row
            hold_var = random.choice(keys[row_val])
            # Add the random value to the encrypt string
            message_encrypt += hold_var
    
    print("\nOriginal Message: " + msg)
    print("\nEncrypted Message: " + message_encrypt)

def homophone_decrypt():
    msg = input("\nEnter Message: ")
    message_decrypt = ""
    
    # Loop through the message 2 letters at a time
    for i in range(0, len(msg), 2):
        for row in range(len(keys)):
            # Supported values
            if msg[i:i+2] in keys[row]:
                # Add corresponding value to the decrypt string
                message_decrypt += symbols[row]
    
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

print("Welcome to the Homophone Cipher machine!")

# Create the key list for this session
create_keys()

# Print generated key set
print("\nHere are the randomized bin values for your cipher text:\n")
for char in symbols:
    print(char.upper() + ":\t" + str(keys[symbols.index(char)]))

run = ""
while run != "q":
    homophone_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Homophone Cipher Program!")
end = input()
