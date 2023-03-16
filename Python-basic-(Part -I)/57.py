# 57. Write a Python program to get the execution time of a Python method.

def calculate_lcm(num1, num2):
    for i in range(max(num1, num2), 1+(num1*num2)):
        if i % num1 == i % num2 == 0:
            lcm = i
            break

    print("LCM of", num1, "and", num2, "is", lcm)


import time
start_time = time.time()
calculate_lcm(24, 6)

print("--- %s seconds ---" % (time.time() - start_time))