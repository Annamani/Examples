# Define a function named 'multiple' that takes two arguments, 'm' and 'n'.
def multiple(m, n):
    # Check if 'm' is a multiple of 'n' by using the modulo operator.
    # If the remainder is 0, return True, indicating 'm' is a multiple of 'n'.
    # Otherwise, return False.
    return True if m % n == 0 else False

print(multiple(20, 5))  
print(multiple(7, 2))   