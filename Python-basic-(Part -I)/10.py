# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

count = 0
n = input("Value: ")
for i in range(1, 4):
    resultant_string = n * i
    count += int(resultant_string)

print(count)