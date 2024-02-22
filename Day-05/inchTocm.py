print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
h_inch += h_ft * 12

# Calculate the height in centimeters by multiplying by the conversion factor (2.54).
h_cm = round(h_inch * 2.54, 1)

# Print the calculated height in centimeters.
print("Your height is : %d cm." % h_cm)
