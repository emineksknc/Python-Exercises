# 51. Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
# These statistics can be formatted into reports via the pstats module.

def check_integer(temp, order):
    if temp.isdigit():
        pass
    else:
        print("Please write an Integer!")
        temp = input(f"Please write {order}. Integer : ")

    return temp


def get_integer(order):
    number = input(f"Please write {order}. Integer : ")
    number_11 = check_integer(number, order=order)
    return number_11


def calculate_gcd(num1, num2):
    gcd = 1
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    print("GCD of", num1, "and", num2, "is", gcd)

def main():
    number_1 = int(get_integer(order=1))
    number_2 = int(get_integer(order=2))
    calculate_gcd(number_1, number_2)


import cProfile

cProfile.run("main()")
