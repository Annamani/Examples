def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thrice(1, 2, 3))

# Call the "sum_thrice" function with the arguments (3, 3, 3) and print the result
print(sum_thrice(3, 3, 3))