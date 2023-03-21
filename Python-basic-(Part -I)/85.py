# 85. Write a Python program to check whether a file path is a file or a directory.


import os

def check_file_or_folder(path):
    if os.path.isfile(path):
        return f"'{path}' is a file!"

    elif os.path.isdir(path):
        return f"'{path}' is a folder!"

    else:
        return f"'{path}' is not file or folder!"


file_path = "../../Python-Exercises/Python-basic-(Part -I)/84.py"
folder_path = "../../Python-Exercises/"
print(check_file_or_folder(file_path))
print(check_file_or_folder(folder_path))
print(check_file_or_folder("test"))
