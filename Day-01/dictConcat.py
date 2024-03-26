# Create three dictionaries 'dic1', 'dic2', and 'dic3' with key-value pairs.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create an empty dictionary 'dic4' that will store the combined key-value pairs from 'dic1', 'dic2', and 'dic3'.
dic4 = {}

# Iterate through each dictionary ('dic1', 'dic2', and 'dic3') using a loop.
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4) 