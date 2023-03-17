# 58. Write a Python program to sum the first n positive integers.


def calculate_sum_of_first_n_integers(n):
    return n * (n+1) / 2


# With Constant Value
print(calculate_sum_of_first_n_integers(7))

# With User Value
count = int(input("Please give an 'n' for sum : "))
print(calculate_sum_of_first_n_integers(count))