# 90. Write a Python program to create a copy of its own source code.

with open("89.py", "r") as file:
    data = file.read()
    with open("temp.py", "w") as temp:
        temp.write(data)
        print(data)

