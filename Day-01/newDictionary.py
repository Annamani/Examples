n=int(input("enter a number to generate a dict: "))
dict_values={}
for x in range(1,n+1):
    dict_values[x]=x*x
print(dict_values)