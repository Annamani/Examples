def test(strs):
    # Use the map function to apply the len function to each string in 'strs', and convert the result to a list
    return [*map(len, strs)]
strs = ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Lengths of the said list of non-empty strings:")
print(test(strs))
strs = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(strs)
print(test(strs))
