# 19. Write a Python program to get a newly-generated string from a given string where "Is"
# has been added to the front. Return the string unchanged if the given string already begins with "Is".
def if_startswith_is(user_string):
    if user_string.startswith("Is"):
        return user_string

    else:
        return 'Is' + user_string


user_string_1 = input("Write a String : ")
print(if_startswith_is(user_string_1))