num=int(input("Enter a number: "))
sum1 = 0
for i in range(1, num):
    if(num % i == 0):
        sum1 = sum1 + i
if (sum1 == num):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")