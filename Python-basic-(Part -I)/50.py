# 50. Write a Python program to print without a newline or space
"""
end=""
sep=""
"""

for i in range(0, 10):
    print('*')


for i in range(0, 10):
    print('*', end="")

print("\n")

print("I", "think", "I", "like", sep="b")
print("I", "think", "I", "like", sep=" ")