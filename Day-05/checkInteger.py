# Define a function 'test' that takes a parameter 'n'.
def test(n):
    # Check if the type of 'n' is equal to 'int'.
    if type(n) == int:
        return "It is an integer!"
    else:
        return "It is a String!"     

print(test(12))
print(test('23312'))
