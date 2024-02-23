d_ft = int(input("Input distance in feet: "))
# 1 foot=12 inches
# 1 yard=3 feet
# 1 yard=36 inches
# 1 mile=1760 yards
# 1 mile=5280 feet
d_inches=d_ft*12
d_yard=d_inches/36
d_mile=d_yard/1760
d_miles=d_ft/5280
print("Distance in Inches: ",d_inches)
print("Distance in Yards: ",d_yard)
print("Distance in Mile using yards: ",d_mile)
print("Distance in Mile using feet: ",d_miles)
