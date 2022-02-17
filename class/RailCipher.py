# Cryoptography

# Ian Fife
# Transposition/Rail Cipher

def rail_cipher():
    mode = input("\nChoose [e] encrypt or [d] decrypt: ")
    message = input("\nEnter Message: ")
    modified_message = message.replace(" ", "")
    
    if mode == "e":
        encrypted_message = ""
        second_half = ""
        index = 0
        for char in modified_message:
            if index % 2 == 0:
                encrypted_message += char
            else:
                second_half += char
            index += 1

        encrypted_message += second_half

        print("\nOriginal Message: " + message)
        print("\nTranslated Message: " + encrypted_message)
    elif mode == "d":
        #Get the second half of the word
        second_half = modified_message[int(len(modified_message)/2 + len(modified_message) % 2):]
        #Get the first half of the word
        first_half = modified_message[0:int(len(modified_message)/2 + len(modified_message) % 2)]

        print(first_half)
        print(second_half)
        decrypted_message = ""
        for i in range(len(second_half)):
            decrypted_message += first_half[i]+ second_half[i]

        if len(first_half) != len(second_half):
            decrypted_message += first_half[-1]
                                
            
        print("\nOriginal Message: " + message)
        print("\nTranslated Message: " + decrypted_message)
    else:
        print("Incorrect value. You must choose either [e] or [d]")


# -- Main --

print("Welcome ot the Rail Cipher Program")

run = ""

while run != "q":
    rail_cipher()
    print(" \n---------------------------------------")
    choice = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Rail Cipher Program!")
end = input()
