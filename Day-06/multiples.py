def multiples(list):
    for item in range(len(list)):
        if item%15==0:
            return item
        



list= [45, 55, 60, 37, 100, 105, 220]
print(multiples(list))