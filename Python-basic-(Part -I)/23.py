# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
# Return n copies of the whole string if the length is less than 2.

words = ["apple", "orange", "an", "a", "the", "banana"]

n=5

for word in words:
    if len(word) > 2 :
        new_word = word[:2]*n + word[2:]
        print(new_word)

    else:
        new_word = word * n
        print(new_word)
