# Define a function to check the type of a variable 'nums'.
def check_type(nums):
    if isinstance(x, tuple) == True:
        return 'The variable x is a tuple'
    elif isinstance(x, list) == True:
        return 'The variable x is a list'
    elif isinstance(x, set) == True:
        return 'The variable x is a set'
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
