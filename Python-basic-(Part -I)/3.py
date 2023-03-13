# 3. Write a Python program to display the current date and time.

from datetime import datetime
time = datetime.now()
print(type(time))
print('Today is ', time.strftime("%d-%m-%Y %H:%M:%S"))