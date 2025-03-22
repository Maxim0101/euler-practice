# Problem 5 : Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive
# number that is evenly divisible (divisible with no remainder) by all 
# of the numbers from 1 to 20?
# ANSWER : 232792560



# WHAT I LEARNED
# 



# MY CODE
def find_smallest_multiple(rangeNum):
    notMultiple = True
    startNumber = rangeNum

    while (notMultiple):
        notMultiple = False
        startNumber += 1
        for i in range(rangeNum):
            if (startNumber % (i + 1) != 0):
                notMultiple = True
                break
    
    return startNumber

# print("ANSWER " + str(find_smallest_multiple(10))) # 2520
# print("ANSWER " + str(find_smallest_multiple(20))) # 232792560


# CHATGPT'S OPTIMIZED VERSION
from math import gcd
from functools import reduce

def lcm(a, b):
    return (a * b) // gcd(a, b)

def GPTfind_smallest_multiple(n):
    return reduce(lcm, range(1, n + 1))

print("ANSWER:", GPTfind_smallest_multiple(10)) # 2520
print("ANSWER:", GPTfind_smallest_multiple(20)) # 232792560
