# 20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.


def return_copies(user_string, number):
    if number >= 1 and len(user_string) > 3:
        return user_string * number

    else:
        print("Check conditions")


print("*****/ Repeat a String \*****")
print("""1. Repeat Number must be greater or equal than 1
2. String length must be greater than 3""")
string = input("Write a String : ")
number = int(input("How many times should the string repeat? : "))
print("Result: ", return_copies(string, number))