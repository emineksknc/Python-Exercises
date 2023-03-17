# 65. Write a Python program that converts seconds into days, hours, minutes, and seconds.

"""
Reference : https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/

    1 day = 86 400 seconds
    1 hour = 3600 seconds
    1 minute = 60 seconds

"""

# Approach 1: Writing a function
# constant variables
day = 86400
hour = 3600
minute = 60
n = 12345

def convert_seconds_to_others(seconds):
    seconds = seconds % day
    hours = seconds // hour
    seconds %= hour
    minutes = seconds // minute
    seconds %= minute

    return "%d:%02d:%02d" % (hours, minutes, seconds)


print(convert_seconds_to_others(n))

# Approach-2: Using Python Standard Library

import datetime


def convert(seconds):
    return str(datetime.timedelta(seconds=seconds))


print(convert(n))
