# Problem 1 : Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
# 23. Find the sum of all the multiples of 3 or 5 below 1000.

# Answer : 233168

# Function: ___

# Time Complexity: O(n) 

# Space Complexity: O(1)

# My Code
def find_multiples_3_and_5_sum(number):
    five_multiple = 0
    three_multiple = 0 
    sum = 0
    
    while three_multiple < number-3:
        three_multiple += 3
        sum += three_multiple

    while five_multiple < number-5:
        if (five_multiple + 5 % 15 == 0):
            five_multiple += 10
        else:
            five_multiple += 5
        sum += five_multiple
    
    return sum

# 150
# 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72 75 78 81 84 87 90 93 96 99 102 105 108 111 114 117 120 123 126 129 132 135 138
# 141 144 147 
# 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145
# Repeats: 15 30 45 60 75 90 105 120 135
# Pattern: every multiple of 15 

# Test Cases
print(find_multiples_3_and_5_sum(10)) # 23
print(find_multiples_3_and_5_sum(1000)) # 233168
