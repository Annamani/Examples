# Define a function named 'perfect_number' that checks if a number 'n' is a perfect number
def perfect_number(n):
    # Initialize a variable 'sum' to store the sum of factors of 'n'
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

print(perfect_number(6)) 
