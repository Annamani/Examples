input_value=input("Enter a input: ")
try:
    a = int(input("Input a number: "))
except ValueError:
    print("\nThis is not a number. Try again...")
    print()