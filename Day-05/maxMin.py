def max_min(data):
    max_value = data[0] 
    min_value = data[0]  
    
    # Iterate through each number 'num' in the 'data' list.
    for num in data:
        # Check if the current number 'num' is greater than the current maximum 'l'.
        if num > max_value:
            max_value = num  # If 'num' is greater, update 'l' with 'num'.
        # Check if the current number 'num' is smaller than the current minimum 's'.
        elif num < min_value:
            min_value = num  # If 'num' is smaller, update 's' with 'num'.
    
    # Return the maximum 'l' and minimum 's' values as a tuple.
    return max_value, min_value

# Call the 'max_min' function with a list of numbers and print the result.
print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
