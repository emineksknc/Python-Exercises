# 82. Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).

item_list = [1, 3, 4, 5, 6]
item_tuple = (1, 3, 4, 5, 6)
item_set = {1, 3, 4, 5,  6}
item_dictionary = {"1": 1, "3": 3, "4": 4, "5": 5, "6": 6}

# print(type(item_list))
# print(type(item_tuple))
# print(type(item_set))
# print(type(item_dictionary))


print(f"List : {item_list} -> {sum(item_list)}")
print(f"Tuple : {item_tuple} -> {sum(item_tuple)}")
print(f"Set : {item_set} -> {sum(item_set)}")
print(f"Dictionary : {item_dictionary} ->{sum(item_dictionary.values())}")