def difference_number(number):
    if number >17:
        result=(number-17)*2
        return result
    else:
        return abs(17-number)

number1=int(input("Enter a number: "))
print(difference_number(number1))
number2=int(input("Enter a number: "))
print(difference_number(number2))
