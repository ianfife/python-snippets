letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar_shift(message, shift):
    new_message = ''
    for i in range(len(message)):
        new_message += letters[(letters.index(message[i]) + shift) % 26]
    return new_message


print(ceasar_shift("zy", 2))
