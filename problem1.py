# Problem 1 : Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
# 23. Find the sum of all the multiples of 3 or 5 below 1000.
# ANSWER : 233168



# WHAT I LEARNED
# - I learned that a much cleaner way to check if a number is a multiple is to use a modulus operator
# - How to compare values between two lists and avoid duplicates
# - That removing items from a list while iterating over it can lead to unexpected behavior



# MY CODE
def find_multiples_3_and_5_sum(number):
    multiples_3 = []
    multiples_5 = []
    x = 0
    y = 0 
    sum = 0
    
    while x < number:
        multiples_3.append(x)
        x += 3

    while y < number:
        multiples_5.append(y)
        y += 5

    for x in multiples_3:
        for y in multiples_5:
            if x == y:
                multiples_3.remove(x)
    
    
    #print(multiples_3)
    #print(multiples_5)
    
    for i in range(len(multiples_3)):
        sum += multiples_3[i]
   
    for j in range(len(multiples_5)):
        sum += multiples_5[j]
    
    return sum

print(find_multiples_3_and_5_sum(10)) #23
print(find_multiples_3_and_5_sum(1000)) #233168



# CHATGPT'S OPTIMIZED VERSION
def GPTfind_multiples_3_and_5_sum(number):
    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

print(GPTfind_multiples_3_and_5_sum(10))   # Output: 23
print(GPTfind_multiples_3_and_5_sum(1000)) # Output: 233168