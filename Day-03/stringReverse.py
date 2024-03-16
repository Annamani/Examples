def string_reverse(str1):
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = len(str1)
    
    # Execute a while loop until 'index' becomes 0
    while index > 0:
        # Concatenate the character at index - 1 of 'str1' to 'rstr1'
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1

print(string_reverse('1234abcd'))
