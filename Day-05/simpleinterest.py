amt = 10000
int = 3.5
years = 7
# FV = P(1 + r/n)^nt.
future_value = amt * ((1 + (0.01 * int)) ** years)
print(round(future_value, 2))