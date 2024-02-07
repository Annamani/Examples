def mul_list(items):
    total = 1
    for x in items:
        total *= x
    return total

# print(mul_list([1, 2, -8]))
print(mul_list([1, 12, 18]))
print(mul_list([-11,-11]))
print(mul_list([0,-11]))
