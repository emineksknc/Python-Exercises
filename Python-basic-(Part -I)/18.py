# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def sum_of_three(number_1, number_2, number_3):
    if number_1 == number_2 == number_3:
        return number_1 * 3
    else:
        return number_1 + number_2 + number_3


number_1 = int(input("Number 1:"))
number_2 = int(input("Number 2:"))
number_3 = int(input("Number 3:"))

print("Result :" , sum_of_three(number_1, number_2, number_3))