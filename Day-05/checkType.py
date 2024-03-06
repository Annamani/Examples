# Define a function to check the type of a variable 'nums'.
def check_type(nums):
    # Check if 'nums' is a tuple and return a message.
    if isinstance(x, tuple) == True:
        return 'The variable x is a tuple'
    # Check if 'nums' is a list and return a message.
    elif isinstance(x, list) == True:
        return 'The variable x is a list'
    # Check if 'nums' is a set and return a message.
    elif isinstance(x, set) == True:
        return 'The variable x is a set'
    # If 'nums' is none of the above types, return a generic message.
    else:
        return 'Neither a list or a set or a tuple.'

x = ['a', 'b', 'c', 'd']
print(check_type(x))
x = {'a', 'b', 'c', 'd'}
print(check_type(x))
x = ('tuple', False, 3.2, 1)
print(check_type(x))
x = 100
print(check_type(x))
