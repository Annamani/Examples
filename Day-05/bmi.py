# Prompt the user to input their height in feet and convert it to a floating-point number.
height = float(input("Input your height in Feet: "))

# Prompt the user to input their weight in kilograms and convert it to a floating-point number.
weight = float(input("Input your weight in Kilograms: "))
bmi= weight / (height * height)
print("BMI is : ",bmi)