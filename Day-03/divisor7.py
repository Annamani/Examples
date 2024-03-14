nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        nl.append(str(x))

# Join the numbers in the list with a comma and print the result
print(','.join(nl))
