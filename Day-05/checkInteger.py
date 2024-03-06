# Define a function 'test' that takes a parameter 'n'.
def test(n):
    if type(n) == int:
        return "It is an integer!"
    else:
        return "It is a String!"     

print(test(12))
print(test('23312'))
