# 70. Write a Python program to sort files by date.
import glob
import os
from pathlib import Path


dirpath = "../Python-basic-(Part -I)"
paths = sorted(Path(dirpath).iterdir(), key=os.path.getctime)
print(paths)

# OR

dirpath = "../Python-basic-(Part -I)/**"
paths = sorted(glob.glob(dirpath), key=os.path.getctime)
print(paths)