# 73. Write a Python program to calculate the midpoints of a line.

def calculate_of_midpoints_of_a_line(first_point: tuple, second_point: tuple):
    x = (first_point[0] + second_point[0]) / 2
    y = (first_point[1] + second_point[1]) / 2
    midpoint = (x, y)

    return midpoint


def main():
    x1 = 4
    y1 = 1
    x2 = 10
    y2 = 5
    print(calculate_of_midpoints_of_a_line((x1, y1), (x2, y2)))


if __name__ == "__main__":
    main()
