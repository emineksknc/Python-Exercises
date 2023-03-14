# 32. Write a Python program to find the least common multiple (LCM) of two positive integers.

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


def calculate_lcm(num1, num2):
    for i in range(max(num1, num2), 1+(num1*num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break

    print("LCM of", num1, "and", num2, "is", lcm)


while 1:
    number_1 = int(get_integer(order=1))
    number_2 = int(get_integer(order=2))
    calculate_lcm(number_1, number_2)
