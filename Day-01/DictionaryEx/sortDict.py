color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

# Iterate through the keys of the 'color_dict' dictionary after sorting them in lexicographical order.
for key in sorted(color_dict):
    # Print each key-value pair where '%s' is a placeholder for the key and its associated color code.
    print("%s: %s" % (key, color_dict[key]))
	