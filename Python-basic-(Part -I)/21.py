# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.
def check_even_or_odd(number):
    if number % 2 == 0:
        message = "Your Number is EVEN!"
        return message
    else:
        message = "Your Number is ODD!"
        return message


print("***** CHECK YOUR NUMBER EVEN OR ODD *****")
user_number = int(input("Write a number : "))
result = check_even_or_odd(user_number)
print(result)