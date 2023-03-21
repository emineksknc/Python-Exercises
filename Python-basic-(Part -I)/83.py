# 83. Write a Python program to test whether all numbers in a list are greater than a certain number.

def check_greater_than(alist, certain_number):
    if all(number > certain_number for number in alist):
        return f"All elements of {alist} are greater than {certain_number}!"

    else:
        return f"All elements of {alist} are NOT greater than {certain_number}!"


numbers_list = [1, 2, 3, 4, 5, 6]
test_number = 10
result = check_greater_than(numbers_list, test_number)
print(result)
