# Define a function named 'perfect_number' that checks if a number 'n' is a perfect number
def perfect_number(n):
    # Initialize a variable 'sum' to store the sum of factors of 'n'
    sum = 0
    
    # Iterate through numbers from 1 to 'n-1' using 'x' as the iterator
    for x in range(1, n):
        # Check if 'x' is a factor of 'n' (divides 'n' without remainder)
        if n % x == 0:
            # If 'x' is a factor of 'n', add it to the 'sum'
            sum += x
    
    # Check if the 'sum' of factors is equal to the original number 'n'
    return sum == n

print(perfect_number(6)) 
