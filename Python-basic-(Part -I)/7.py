# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
import os

user_data = input("Write filename : ")
file_name, file_extension = os.path.splitext(user_data)
print("File Extension :", file_extension[1:])