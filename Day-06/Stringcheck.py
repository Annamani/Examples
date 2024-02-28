text = input("Input a word or numbers: ")
if text.isdigit():
    # If the input contains only digits, print "The input value is numbers."
    print("The input value is numbers.")
else:
    # If the input contains characters other than digits, print "The input value is string."
    print("The input value is string.")
