# 91. Write a Python program to swap two variables.


# Solution-1
x = 30
y = 20
print("Solution-1")
print("Before Swaping : ", x , y)

temp = y
y = x
x = temp
print("After Swaping : ", x , y)

# Solution-2
x = 30
y = 20
print("Solution-2")
print("Before Swaping : ", x , y)
x,y = y,x
print("After Swaping : ", x , y)
