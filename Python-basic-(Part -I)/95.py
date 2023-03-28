#95. Write a Python program to check whether a string is numeric.

def check_a_string_is_numeric(string:str):
    if string.isnumeric():
        print(f"\"{string}\" is numeric !")

    else:
        print(f"\"{string}\" is not numeric!")


word = "Hello"
numeric_word = "1234"
check_a_string_is_numeric(word)
check_a_string_is_numeric(numeric_word)

