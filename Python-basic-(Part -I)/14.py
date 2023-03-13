# 14. Write a Python program to calculate the number of days between two dates.


from datetime import datetime
date_format = "%m/%d/%Y"
date1 = input(f"Please enter first date Month/Day/Year: ")
date2 = input(f"Please enter  second date Month/Day/Year: ")

a = datetime.strptime(date1, date_format)
b = datetime.strptime(date2, date_format)
delta = abs(b - a)

print(delta.days) # that's it