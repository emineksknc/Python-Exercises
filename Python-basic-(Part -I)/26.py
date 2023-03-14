# 26. Write a Python program to create a histogram from a given list of integers.

integers = [4, 4, 4, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5, 6, 7, 9, 9, 9]
output = []

for integer in integers:
    if integer not in output:
        output.append(integer)
for integer in output:
    print(integer, '*' * integers.count(integer))