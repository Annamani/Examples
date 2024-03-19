# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    # Create an empty list 'x' to store unique elements
    x = []
    
    # Iterate through each element 'a' in the input list 'l'
    for a in l:
        # Check if the element 'a' is not already present in the list 'x'
        if a not in x:
            x.append(a)
    return x
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  
