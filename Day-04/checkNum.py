def check_num(group_data, n):
    for value in group_data:
        if n == value:
            return True  
    return False  

print(check_num([1, 5, 8, 3], 3)) 
print(check_num([5, 8, 3], -1))
