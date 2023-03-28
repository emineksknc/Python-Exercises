# 96. Write a Python program to print the current call stack.

import traceback

# A solution
traceback.print_stack()


# Solution with functions
def f():
    g()


def g():
    for line in traceback.format_stack():
        print(line.strip())


f()
