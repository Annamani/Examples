# Create an empty list to store formatted numbers.
numbers = []

# Iterate through numbers from 0 to 999 (exclusive).
for num in range(1000):
    # Convert the number to a string and fill with zeros to make it three digits long.
    num = str(num).zfill(3)
print(num)
numbers.append(num)
