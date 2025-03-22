# Problem 4 : Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome
# made from product of two 2-digit numbers is 9009 = 91 x 99. Find
# the largest palindrome made from the product of two 3-digit numbers.
# ANSWER : 906609



# WHAT I LEARNED
# 



# MY CODE
def find_largest_number_palindrome(digit_length):
    # creates two numbers highest numbers which is based off given digit_length
    highest_number = ""
    for i in range(digit_length):
        highest_number += "9"
    num1 = int(highest_number)
    num2 = int(highest_number)
    largest_palindrome = 0

    # finds the largest palindrome with 2 given numbers
    while (num1 > 0):
        current_product = num1 * num2
        if (is_palindrome(str(current_product)) and largest_palindrome < current_product):
            largest_palindrome = current_product
        
        while (num2 > 0):
            num2 -= 1
            current_product = num1 * num2
            if (is_palindrome(str(current_product)) and largest_palindrome < current_product):
                largest_palindrome = current_product
        # set num2 = num1 to avoid duplicate multiplcation
        num2 = num1
        num1 -= 1

    return largest_palindrome

# checks if the multiplication of two numbers is a palindrome
def is_palindrome(product):
    product_len = len(product) // 2

    for i in range(product_len):
       if product[i] != product[len(product)-i-1]:
           return False
    return True

print(find_largest_number_palindrome(2)) #9009
print(find_largest_number_palindrome(3)) #906609
# print(find_largest_number_palindrome(4)) #99000099



# CHATGPT'S OPTIMIZED VERSION
def GPTfind_largest_number_palindrome(digit_length):
    # Create the largest and smallest numbers with the given digit length
    highest_number = int("9" * digit_length)
    lowest_number = 10 ** (digit_length - 1)

    largest_palindrome = 0

    # Loop downwards to maximize early largest palindrome detection
    for num1 in range(highest_number, lowest_number - 1, -1):
        for num2 in range(num1, lowest_number - 1, -1):  # Start num2 from num1 to avoid duplicate pairs
            product = num1 * num2
            if product <= largest_palindrome:
                break  # No need to check further; products will only get smaller
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

# Optimized palindrome check
def GPTis_palindrome(number):
    return str(number) == str(number)[::-1]  # Simple and efficient
