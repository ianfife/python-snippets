# Ian Fife
# 4/6/2022

# Vigenere Cipher V2
# This program encrypts and decrypts messages using the vigenere cipher.
# Messages are encrypted and decrypted using a lookup table.


lookup_table = [[]]  # 2-D array for Vigenere Squaree
symbols = 'abcdefghijklmnopqrstuvwxyz'

def create_table():
    table_symbols = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(table_symbols)):
        for char in table_symbols:
            lookup_table[i].append(char)
        table_symbols = table_symbols[1:len(table_symbols)] + table_symbols[0]
        if i < len(table_symbols) - 1:
            lookup_table.append([])
    
def create_key_word_list(key_word, plain_text):
    key_word_index = 0
    key_word_list = ""
    
    for char in plain_text:
        if char in symbols:
            key_word_list += key_word[key_word_index % len(key_word)]
            key_word_index += 1
    return key_word_list

def vigenere_cipher():
    # Get mode from the user: 
    mode = input("\nChoose [e] encrypt or [d] decrypt: ").lower()

    while mode not in ['e', 'd']:
        mode = input("\nInvalid Input -- Choose [e] encrypt or [d] decrypt: ").lower()

    # Get message from the user:
    plain_text = input("\nEnter Message: ").lower()

    # Get key word from the user:
    key_word = input("\nEnter Key Word: ").lower()

    key_word_list = create_key_word_list(key_word, plain_text)
    
    if mode == 'e':
        print("\nYour encrypted message is: " + encrypt(key_word_list, plain_text))
    else:
        print("\nYour decrypted message is: " + decrypt(key_word_list, plain_text))

def encrypt(key_word_list, plain_text):
    cipher_text = ""
    key_word_index = 0
    
    for char in plain_text:
        if char in symbols:
            cipher_text += lookup_table[symbols.index(char)][symbols.index(key_word_list[key_word_index])]
            print(symbols.index(char))
            print(symbols.index(key_word_list[key_word_index]))
            print(lookup_table[symbols.index(char)])
            key_word_index += 1
        else:
            cipher_text += char

    return cipher_text

def decrypt(key_word_list, cipher_text):
    plain_text = ""
    key_word_index = 0
    
    for char in cipher_text:
        if char in symbols:
            textLetter = find_row_val(key_word_list[key_word_index], char)
            key_word_index += 1
            plain_text += textLetter
        else:
            plain_text += char
    return plain_text

def find_row_val(key_letter, text_letter):
    return_letter = ""
    for char in lookup_table[symbols.index(key_letter)]:
        if char == text_letter:
            return_letter = symbols[lookup_table[symbols.index(key_letter)].index(char)]
    return return_letter

# -------------------------------------------------------

# Main Program

print("Welcome to the Vigenere Cipher Program!")

create_table()

choice = ''
while choice != 'q':
    vigenere_cipher()
    print("---------------------------------------")
    choice = input("Press ENTER to continue, 'q' to quit: ")
    print("---------------------------------------")

print("\nThanks for using the Vigenere Cipher Program!")
end = input()
