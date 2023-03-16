# 52. Write a Python program to print to STDERR.

import sys
print('Hello world', file=sys.stderr)