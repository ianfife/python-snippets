import random

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
    msg = input("Enter Message: ").lower()
    message_encrypt = ""
    for char in msg:
        if char in char_list:
            row_val = char_list.index(char)
            hold_var = random.choice(value_list[row_val])
            message_encrypt += hold_var
    print("Original Message: " + msg)
    print("Encrypted Message: " + message_encrypt)

def homophone_cipher():
    mode = input("\nEnter [e] for encrypt or [d] for decrypt: ").lower()
    while mode not in ['e', 'd']:
        mode = input("\n --Invalid Input-- Enter [e] for encrypt or [d] for decrypt: ").lower()

    if mode == 'e':
        homophone_encrypt()
    else:
        pass
        #homophone_decrypt()

## -- Main --

print("Welcome to the Homophone Cipher Program!")

run = ""
while run != "q":
    homophone_cipher()
    print("\n---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Baconian Cipher Program!")
end = input()