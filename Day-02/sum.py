def cubeof(number):
    return number*number*number

number=input("Enter a number: ")
total=number+pow(number)+cubeof(number)
print("Sum of power and cube of numbers: ",total)