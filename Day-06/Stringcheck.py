# Doesn't work for floats
# Prompt the user for input and store it in the 'text' variable.
text = input("Input a word or numbers: ")

# Check if the input consists of digits only using the 'isdigit' method.
if text.isdigit():
    # If the input contains only digits, print "The input value is numbers."
    print("The input value is numbers.")
else:
    # If the input contains characters other than digits, print "The input value is string."
    print("The input value is string.")
