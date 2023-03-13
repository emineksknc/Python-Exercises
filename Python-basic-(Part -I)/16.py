# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference

def difference(number):
    if number > 17:
        return 2 * abs(17-number)

    else:
        return 17-number


number = int(input("Give a Number : "))

print(difference(number))
