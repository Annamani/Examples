myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original Dictionary: \n",myDict)
if 'a' in myDict:
    del myDict['a']

# Print the updated dictionary 'myDict' after deleting the key 'a' (if it existed).
print(myDict)