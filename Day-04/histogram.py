def histogram(numbers):
    for n in numbers:
        output = ''  
        times = n            
        # Use a while loop to append '*' to the output string 'times' number of times.
        while times > 0:
            output += "@"
            times = times - 1  # Decrement the times variable.
        
        # Print the resulting output string.
        print(output)



histogram([2, 3, 6, 5])