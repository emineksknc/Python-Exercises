# 27. Write a Python program that concatenates all elements in a list into a string and returns it.
integers = [4, 4, 4, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5, 6, 7, 9, 9, 9]
output = ''

for i in integers:
    output += str(i)

print(output)