# 8. Write a Python program to display the first and last colors from the following list. color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red", "Green","White" ,"Black"]

# Approach-1 Slicing

print('The first and last element of list are : ', color_list[0], color_list[len(color_list)-1])

# Approach-2 Mapping
index_list = [0, len(color_list)-1]
res = map(color_list.__getitem__, index_list)

# printing result
print('The first and last element of list are : ', *res)