# 40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""
https://byjus.com/maths/distance-between-two-points-formula/#:~:text=Distance%20between%20two%20points%20is,coordinate%20plane%20or%20x%2Dy%20plane.


"""
import math


def calculate_distance_of_two_points(p1, p2):
    Xs_difference = p1[0] - p2[0]
    Ys_difference = p1[1] - p2[1]
    result = math.sqrt(abs(Xs_difference) ** 2 + abs(Ys_difference) ** 2)
    return result


point1 = (3, 4)
point2 = (4, 5)

# First Approach
print(calculate_distance_of_two_points(point1, point2))

# Second and Simple Approach
print(math.dist(point1, point2))
