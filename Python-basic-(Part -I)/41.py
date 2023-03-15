# 41. Write a Python program to check whether a file exists.

import os


def check_file(file_name):
    if os.path.exists(file_name):
        return True

    else:
        return False


print(check_file("22.py"),
      "\n",
      check_file("abc.java"))
