# 25. Write a Python program that checks whether a specified value is contained within a group of values

def check_number(number):
    numbers = [1, 5, 8, 3]
    if number in numbers:
        print("True")

    else:
        print("False")


while 1:
    n = int(input("Write a number : "))
    check_number(n)


