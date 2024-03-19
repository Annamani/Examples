# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  
