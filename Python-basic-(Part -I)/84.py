# 84. Write a Python program to count the number of occurrences of a specific character in a string.

def count_character(string, character):
    count = string.count(character)
    if count > 0:
        return f"{string} contains '{character}' character {count} times!"

    else:
        return f"{string} don't contains '{character}' character!"


sample_string = "Python Exercises"
sample_character = "E"
print(count_character(sample_string, sample_character))
