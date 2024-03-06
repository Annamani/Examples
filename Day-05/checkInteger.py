# Define a function 'test' that takes a parameter 'n'.
def test(n):
    # Check if the type of 'n' is equal to 'int'.
    if type(n) == int:
         # If 'n' is an integer, return the message "It is an integer!"
         return "It is an integer!"
    else:
         # If 'n' is not an integer, return the message "It is a String!"
         return "It is a String!"     

print(test(12))
print(test('23312'))
