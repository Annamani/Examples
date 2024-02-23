num=int(input("Enter a number: "))
sum=0
while num>0:
    units=num%10
    sum=sum+num
    num=num/10

print("Sum of numbers in an integer: ",sum)