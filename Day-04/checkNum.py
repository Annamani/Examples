def check_num(group_data, n):
    for value in group_data:
        if n == value:
            return True  # If found, return True.
    return False  # If the loop completes and no match is found, return False.

print(check_num([1, 5, 8, 3], 3)) 
print(check_num([5, 8, 3], -1))
