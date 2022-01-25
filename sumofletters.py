def sum_of_letters(word):
    letters = "abcdefghijklmnopqrstuvwxyz"
    value = 0
    for char in word:
        value += letters.index(char) + 1
    return value

main = "y"

while(main.lower() == "y"):
    word = input("Enter a word: ")
    print("The word " + word + " has a value of " + str(sum_of_letters(word)))
    main = input("Would you like to enter another word? (Y/N) ")
