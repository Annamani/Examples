def sum_list(items):
    sum_numbers = 0
    for x in items:
        # Add the current element 'x' to the 'sum_numbers' variable
        sum_numbers += x
    # Return the final sum of the numbers
    return sum_numbers

# Call the sum_list function with the list [1, 2, -8] as input and print the result
print(sum_list([1, 2, -8]))
