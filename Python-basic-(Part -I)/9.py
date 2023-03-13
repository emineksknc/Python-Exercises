# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = input("Write your examination schedule (format : (11, 12, 2014) : ")

remove_list = ['(', ')']

for ch in remove_list:
    exam_st_date = exam_st_date.replace(ch, '')

print("The examination will start from :", exam_st_date.replace(',' ,' /'))
