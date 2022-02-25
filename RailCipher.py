# Cryoptography

# Ian Fife
# Transposition/Rail Cipher
# This program performs both encryption and decryption with
# a key 2 rail cipher. One important note is that it removes
# spaces.

def rail_cipher():
    mode = input("\nChoose [e] encrypt or [d] decrypt: ")
    
    if mode == "e":
        # Get user input and remove spaces
        message = input("\nEnter Message: ")
        modified_message = message.replace(" ", "")
        encrypted_message = ""
        second_half = ""
        index = 0
        for char in modified_message:
            # Test if we are on an odd or even character
            if index % 2 == 0:
                # Add even characters to final string
                encrypted_message += char
            else:
                # Add odd characters to a secondary string
                # which will be appended later.
                second_half += char
            index += 1
        # Append second half
        encrypted_message += second_half

        print("\nOriginal Message: " + message)
        print("\nTranslated Message: " + encrypted_message)
    elif mode == "d":
        # Get user input and remove spaces
        message = input("\nEnter Message: ")
        modified_message = message.replace(" ", "")
        # Get the second half of the word
        second_half = modified_message[int(len(modified_message)/2 + len(modified_message) % 2):]
        # Get the first half of the word
        first_half = modified_message[0:int(len(modified_message)/2 + len(modified_message) % 2)]
        # If the length of the entire message ends up being odd,
        # the extra character goes into the first half.

        decrypted_message = ""
        # Add the letters simultaneously
        for i in range(len(second_half)):
            decrypted_message += first_half[i] + second_half[i]

        # When the messages length ends up odd, this is necessary
        # to add the final letter to prevent index out of bounds
        # errors in the above loop.
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
    run = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Rail Cipher Program!")
end = input()
