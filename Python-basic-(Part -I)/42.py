# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

# 1. Approach
import platform
print(platform.architecture())

# 2. Approach
import struct
print(struct.calcsize("P") * 8)