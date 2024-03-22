# Define a function named 'printValues' that generates a list of squares of numbers from 1 to 20
def printValues():
    # Create an empty list 'l'
    l = list()
    for i in range(1, 21):
        l.append(i**2)
print(l)
printValues()