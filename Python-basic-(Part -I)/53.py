# 53. Write a Python program to access environment variables.

import os

# 3 ways of accessing environment variables
print(os.environ['HOME'])
print(os.environ.get('HOME'))
print(os.getenv('HOME'))

print(os.environ)
print(os.environ.get('HOME', '/home/username/'))


# Returns `default_value` if the key doesn't exist
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

# Returns `default_value` if the key doesn't exist
print(os.getenv('KEY_THAT_MIGHT_EXIST'))



