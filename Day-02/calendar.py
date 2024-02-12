import calendar

obj = calendar.Calendar()
# Prompt the user to input the year and month
year = int(input("Input the year : "))
month = int(input("Input the month : "))

# printing with monthdatescalendar
print(obj.monthdatescalendar(year, month))