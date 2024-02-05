str_1 = input ("Enter a string: ")
words = [word.lower () for word in str_1.split ()]
# Print the words in alphabetical order
words.sort ()
print("The words sorted in alphabetical order are as follows: ")
for word in words:
    print(word)