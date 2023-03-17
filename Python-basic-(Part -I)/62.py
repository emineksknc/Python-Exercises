# 62. Write a Python program to convert all units of time into seconds.
import time


def convert_current_time_into_seconds(current_time):
    print("Date :", time.asctime(time.localtime()))
    print("The amounts of seconds of current date: ", current_time)


def convert_given_time_into_seconds(day, hour, minute, second):
    days = day*3600*24
    hours = hour*3600
    minutes = minute*60
    seconds = second
    total_seconds =  days+hours+minutes+seconds
    print("The amounts of seconds of given date: ", total_seconds)


convert_current_time_into_seconds(time.time())
convert_given_time_into_seconds(day=5, hour=10, minute=2, second=1 )
