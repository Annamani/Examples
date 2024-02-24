# Print a message to inform the user that the program will calculate the midpoint of a line.
print('\nCalculate the midpoint of a line :')

# Prompt the user to enter the x and y coordinates of the first endpoint of the line.
x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

# Prompt the user to enter the x and y coordinates of the second endpoint of the line.
x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x=(x1+x2)/2
y=(y1+y2)/2

print("Midpoint of a line is : ",x,y)
