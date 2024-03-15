def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

def multiply(numbers):
    mul_value = 1
    for x in numbers:
        mul_value *= x
    return mul_value

print(sum((8, 2, 3, 0, 7)))
print(multiply((8, 2, 3, -1, 7)))

