# Define a function named 'is_even_num' that takes a list 'l' as input and returns a list of even numbers
def is_even_num(l):
    # Create an empty list 'enum' to store even numbers
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9])) 
