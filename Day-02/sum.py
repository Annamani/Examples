number1=int(input("Enter a number: "))
number2=int("%s%s" % (number1, number1))
number3 = int("%s%s%s" % (number1, number1, number1))
print("Sum of (n+nn+nnn)numbers: ",number1+number2+number3)