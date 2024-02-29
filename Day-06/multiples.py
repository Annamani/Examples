def multiples(list):
    for item in range(len(list)):
        if item%15==0:
            return item
        



list= [45, 55, 60, 37, 100, 105, 220]
# result = list(filter(lambda x: (x % 13 == 0), list))
# print(result)
print(multiples(list))