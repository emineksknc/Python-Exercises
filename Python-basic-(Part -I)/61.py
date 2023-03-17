# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.


# Contant Variables
inches = 12
yards = 0.3333333333
miles = 0.0001893939


def calculate_feet_to_others(feet):
    feet_to_inches = feet*inches
    feet_to_yards = feet*yards
    feet_to_miles = feet*miles

    return f'{feet} feet = {feet_to_inches} inches\n{feet} feet = {feet_to_yards} yards\n{feet} feet = {feet_to_miles} miles'


feet = float(input("Give a Feet : "))
print(calculate_feet_to_others(feet))