# 34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def sum_of_two_integers(int1, int2):
    summation = int1 + int2
    if 15 < summation < 20:
        return 20

    else:
        return summation


while 1:
    num1 = int(input("1. Number: "))
    num2 = int(input("2. Number: "))
    summation = sum_of_two_integers(num1, num2)

    print(f"Sum : ", summation)
