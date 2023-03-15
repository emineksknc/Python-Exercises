#36. Write a Python program to add two objects if both objects are integers.

def sum_two_objects_if_both_are_integers(object1, object2):
    if object1.isnumeric() and object2.isnumeric():
        sum = int(object1) + int(object2)

        return f"Sum of {object1} and {object2} : {sum}"

    else:
        return f"Please, Write Numeric Values!"

while 1:
    obj1 = input("1. Entry : ")
    obj2 = input("2. Entry : ")
    print(sum_two_objects_if_both_are_integers(obj1, obj2))
