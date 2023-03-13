# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
print("Please write numbers with comma example: 3, 5, 7, 23")
user_string = input("Write your number:")
numbers_list = user_string.split(",")
print("List: ", numbers_list)

numbers_tuple = tuple(number for number in numbers_list)

print("Tuple: ", numbers_tuple)