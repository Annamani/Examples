def max_min(data):
    max_value = data[0] 
    min_value = data[0]  
    
    for num in data:
        if num > max_value:
            max_value = num  
        elif num < min_value:
            min_value = num  
    
    return max_value, min_value

# Call the 'max_min' function with a list of numbers and print the result.
print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
