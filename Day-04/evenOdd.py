def evenOdd(number):
    if number==0 or number==1:
        print(number," is neither even nor odd number")
    elif number%2==0:
        print(number," is a Even number")
    else:
        print(number, " is a Odd number")

num=int(input("Enter a number: "))
print(evenOdd(num))