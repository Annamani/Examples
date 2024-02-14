def list_count(list):
    count=0
    for num in list:
        if num==4:
            count+=1
    return count

print(list_count([1, 4, 6, 7, 4])) 
print(list_count([1, 4, 6, 4, 7, 4])) 