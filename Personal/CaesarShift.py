def caesar_shift(message, shift):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_message = ''
    message = message.lower()
    for char in message:
        if char == " ":
            new_message += " "
        else:
            new_message += letters[(letters.index(char) + shift) % 26]
    return new_message


print(caesar_shift("Hello World", 2))
