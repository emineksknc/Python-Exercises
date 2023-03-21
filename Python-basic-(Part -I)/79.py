# 79. Write a Python program to get the size of an object in bytes
"""

Have a look : https://www.geeksforgeeks.org/how-to-find-size-of-an-object-in-python/

"""

import sys

print("Integer : ", sys.getsizeof(4))
print("String : ", sys.getsizeof("4"))
print("Float : ", sys.getsizeof(4.0))
print("Empty List : ", sys.getsizeof([]))
print("List : ", sys.getsizeof([4, 8, 1]))
print("Empty Tuple : ", sys.getsizeof(()))
print("Tuple : ", sys.getsizeof((4, 8, 1)))
print("Empty Set : ", sys.getsizeof({}))
print("Set : ", sys.getsizeof({4, 8, 1}))
print("Dictionary : ", sys.getsizeof({"name": "emine", "surname":"kiskanc"}))