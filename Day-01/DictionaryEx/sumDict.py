my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
# result = sum(my_dict.values())
# print(result)
sum=0
for value in my_dict.values():
    sum=sum+value
print(sum)