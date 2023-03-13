# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def athousand_or_twothousand(number):
    return abs(1000-number) <= 100 or abs(2000-number) <= 100


print("/---/ Test whether a number is within 100 of 1000 or 2000 /---/")
while 1:
    number = int(input("Give a number : "))
    print(athousand_or_twothousand(number))
