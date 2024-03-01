input_value=input("Enter a input: ")
try:
    a = int(input("Input a number: "))
    break
except ValueError:
        # If the input is not a valid integer, an exception (ValueError) is raised.
        # In that case, print an error message and prompt the user to try again.
        print("\nThis is not a number. Try again...")
        print()