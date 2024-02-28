def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
print("Before swapping: ",a,b)
print("after swapping: ",swap(a,b))
