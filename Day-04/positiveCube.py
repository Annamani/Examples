def cubeOfPositiveNumber(num):
    sum=0
    number=n-1
    while(number>0):
        sum+=number*number*number
    return sum

num=int(input("Enter a positive number: "))
print(cubeOfPositiveNumber(num))