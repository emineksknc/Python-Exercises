# 33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum_of_three_integers(int1, int2, int3):
    if int1 == int2 or int1 == int3 or int2 == int3:
        return 0

    else:
        return int1 + int2 + int3


while 1:
    num1 = int(input("1. Number: "))
    num2 = int(input("2. Number: "))
    num3 = int(input("3. Number: "))
    summation = sum_of_three_integers(num1, num2, num3)

    print(f"Sum : ", summation)
