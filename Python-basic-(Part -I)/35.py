# 35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

def two_integers(int1, int2):
    if int1 == int2 or (int1 + int2) == 5 or abs(int1 - int2) == 5:
        return True

    else:
        return False


while 1:
    num1 = int(input("1. Number: "))
    num2 = int(input("2. Number: "))
    summation = two_integers(num1, num2)

    print(f"Sum : ", summation)
