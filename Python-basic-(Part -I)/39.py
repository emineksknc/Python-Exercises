# 39. Write a Python program to compute the future value of a specified principal amount,
# rate of interest, and number of years.


"""
    Future Value Formula:
        https://www.wallstreetprep.com/knowledge/future-value-fv/

"""

principal_amount = 10000
rate_of_interest = 3.5
years = 7
FV = principal_amount * (1 + rate_of_interest/100) ** years
print(FV)
