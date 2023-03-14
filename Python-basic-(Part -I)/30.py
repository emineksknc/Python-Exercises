# 30. Write a Python program that will accept the base and height of a triangle and compute its area.

def calculate_triangle_area(base, height):
    return base*height/2

print("/*** Calculate Triangle Area \***")

base = float(input("Base : "))
height = float(input("Height : "))

print(calculate_triangle_area(base, height))
