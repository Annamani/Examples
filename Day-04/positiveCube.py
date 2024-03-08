def cubeOfPositiveNumber(num):
    sum=0
    number=num-1
    while(number>0):
        sum+=number*number*number
        number=number-1
    return sum

num=int(input("Enter a positive number: "))
print(cubeOfPositiveNumber(num))