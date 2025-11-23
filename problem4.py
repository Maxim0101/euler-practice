# Problem 4 : Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome
# made from product of two 2-digit numbers is 9009 = 91 x 99. Find
# the largest palindrome made from the product of two 3-digit numbers.
# ANSWER : 906609



# WHAT I LEARNED
# - How to use string reversal and indexing to check if a number is a palindrome
# - How to work with digit-based limits by dynamically constructing numbers like 999, 9999, etc.
# - How nested loops can generate all pairwise products efficiently
# - How to keep track of the largest value conditionally during iteration
# - That breaking out of a loop early can improve performance once further results are guaranteed to be smaller
# - That Python has powerful built-in string operations like [::-1] for quick checks and cleaner code which I forgot about



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