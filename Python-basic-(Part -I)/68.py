# 68. Write a Python program to calculate sum of digits of a number.

def sum_of_digits_a_number(number):
    str_num = str(number)
    digit_list = [*str_num]
    total_sum = 0
    for digit in digit_list:
        total_sum += int(digit)

    return total_sum


def main():
    number = 15943121
    result = sum_of_digits_a_number(number)
    print(f'Sum of digits of {number} is {result}')


if __name__ == "__main__":
    main()
