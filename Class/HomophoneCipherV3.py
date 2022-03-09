# Ian Fife
# 3/7/2022

# Homophone Cipher V3
# This program encrypts and decrypts messages using the homophone
# cipher. Symbols are defined with a group of correlating values
# in order to counter frequency analysis. In V2, the key is randomly
# generated each time. In V3, a header is created in order to decrypt
# messages using the previously generated key.

import random

# Symbol set and corresponding data
symbols = "abcdefghijklmnopqrstuvwxyz "

keys = [[8], [2], [3], [4], [11], [2], [2], [6], [6],
              [1], [1], [4], [2], [6], [7], [2], [1], [6],
              [6], [9], [3], [1], [2], [1], [2], [1], [1]]

# All possible values
values = ["00", "01", "02", "03", "04", "05",
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

def homophone_encrypt():
    
    def write_header():
        keys_copy = keys
        values_copy = values
        
        # Loop through each row
        for row in keys_copy:
            # Grab the bin size stored in the keys 2d array
            bin_size = row.pop(0)
            for i in range(bin_size):
                # Append a randomly chosen value from the values_copy
                # list to the header string and remove that value
                # as an option
                row.append(values_copy.pop(values_copy.index(random.choice(values_copy))))
                
        return keys_copy

    
    msg = input("\nEnter Message: ").lower()
    keys_copy = write_header()
    message_encrypt = ""
    
    for row in keys_copy:
        for val in row:
            message_encrypt += val
    
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
    
    def read_header(msg):
        keys_copy = keys
        position = 0
        
        # Loop through each row
        for row in keys_copy:
            # Grab the bin size stored in the keys_copy 2d array
            bin_size = row.pop(0)
            for i in range(bin_size):
                # Append the values in the header to their corresponding row
                row.append(msg[position:position+2])
                position += 2
                
        return keys_copy

    
    msg = input("\nEnter Message: ")
    message_decrypt = ""

    keys_copy = read_header(msg)
    keys_copy_length = 0
    
    for row in keys_copy:
        keys_copy_length += len(row)

    print(keys_copy)
    
    # Loop through the message 2 letters at a time
    for i in range(keys_copy_length, len(msg), 2):
        for row in range(len(keys_copy)):
            # Supported values
            if msg[i:i+2] in keys_copy[row]:
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

print("Welcome to the Homophone Cipher Program!")

# Create the key list for this session
run = ""
while run != "q":
    homophone_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Homophone Cipher Program!")
end = input()
