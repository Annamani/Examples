# Define the principal amount (initial investment).
amt = 10000
# Define the annual interest rate as a percentage.
int = 3.5
# Define the number of years.
years = 7
# FV = P(1 + r/n)^nt.
future_value = amt * ((1 + (0.01 * int)) ** years)
print(round(future_value, 2))