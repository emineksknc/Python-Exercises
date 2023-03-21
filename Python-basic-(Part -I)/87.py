# 87. Write a Python program to get the size of a file.

# Solution-1
import os
path = '../Python-basic-(Part -I)/81.py'
print(os.path.getsize(path))

# Solution-2
from pathlib import Path
print(Path(path).stat().st_size)

# Solution-3
import os
print(os.stat(path).st_size)