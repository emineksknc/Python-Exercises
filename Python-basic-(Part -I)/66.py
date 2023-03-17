# 66. Write a Python program to calculate the body mass index.
"""
Reference : https://www.calculator.net/bmi-calculator.html?ctype=metric&cage=25&csex=m&cheightfeet=5&cheightinch=10&cpound=160&cheightmeter=180&ckg=95&printit=0&x=67&y=28
"""


def BMI_control(BMI):
    if BMI < 18.5:
        print("You are Underweight!")
    elif 18.5 <= BMI < 25:
        print("You are Normal!")

    elif 25 <= BMI < 30:
        print("You are Overweight!")

    elif 30 <= BMI < 35:
        print("You are almost Obese!")

    elif 35 <= BMI:
        print("You are Obese!")

while 1:
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    BMI = weight / (height / 100) ** 2
    print(f"You BMI is {round(BMI, 2)}")
    BMI_control(BMI)

