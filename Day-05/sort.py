# a,b,c=8,3,7
# maxn=a
# minn=b
# middle=(a+b+c)-maxn-minn
# print("Sort: ",minn,middle,maxn)


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
max_number=max(a,b,c)
min_number=min(a,b,c)
middle_number=(a+b+c)-max_number-min_number
print("After sorting of numbers: "min_number,middle_number,max_number)