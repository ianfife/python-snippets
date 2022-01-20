message = input("Enter text: ")
shift = int(input("Enter shift: "))

message_lowercase = message.lower()
new_string = ""

for char in message_lowercase:
    ordChar = ord(char)
    ordChar += shift
    while ordChar > 122:
        ordChar -= 26
    ordChar = chr(ordChar)
    new_string += ordChar

print(message)
print(new_string)