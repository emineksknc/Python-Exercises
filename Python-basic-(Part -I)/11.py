# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

built_in_function_name = input("Write built-in function name : ")

print(eval(built_in_function_name).__doc__)