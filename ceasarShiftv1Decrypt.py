message = input("Enter text: ")
shift = int(input("Enter shift: "))

message_lowercase = message.lower()
shiftedChars = ""

for char in message_lowercase:
    ordChar = ord(char)
    ordChar -= shift
    while ordChar < 97:
        ordChar += 26
    ordChar = chr(ordChar)
    shiftedChars += ordChar

print(message)
print(shiftedChars)

end = input()
