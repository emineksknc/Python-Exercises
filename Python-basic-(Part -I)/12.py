# 12. Write a Python program that prints the calendar for a given month and year.


# import module
import calendar


print("***** CALENDAR *****")
year = int(input("Please write year: "))
month = int(input("Please write month: "))
if month >= 13:
    print("--Please write correct month number!")
    month = int(input("Please write month: "))

# display the calendar
print(calendar.month(year, month))