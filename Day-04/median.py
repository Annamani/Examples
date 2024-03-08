x = input("Input the first number: ")

# Input the second number from the user
y = input("Input the second number: ")

# Input the third number from the user
z = input("Input the third number: ")

# Print a message indicating that the program will calculate the median
print("Median of the above three numbers -")

# Check conditions to determine the median and print the result
if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)
elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)
elif y < z and z < x:
    print(z)    
elif x < z and z < y:
    print(z)
