# Ian Fife
# 2/22/2022

# Baconian Cipher V1
# This Program encrypts and decrypts messages
# using the Baconian Cipher. It substitutes letters
# with a string of five binary digits.

def baconian_cipher():
    # Symbol set
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    message = input("\nEnter Message: ")

    while mode != "e" or mode != "d":
        mode = input("/nChoose [e] encrypt or [d] decrypt: ")
        if mode = "e":
            for char in message:
                
        elif mode = "d":

        else:
            print("\nIncorrect value. You must enter [e] or [d].")

# -- Main --

run = ""

while run != "q":
    baconian_cipher()
    print("---------------------------------------")
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Baconian Cipher Program!")
end = input()
