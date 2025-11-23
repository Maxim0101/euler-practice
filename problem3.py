# Problem 3 : Largest Prime Factor
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143
# ANSWER : 6857



# WHAT I LEARNED
# - How to find the largest prime factor of a number through repeated division
# - That prime factorization involves checking divisibility from smallest primes upward
# - How to implement both iterative and recursive solutions to a problem
# - That checking up to the square root of a number is more efficient than up to n/2 or n
# - How to manage while loop conditions and update multiple variables
# - That optimizing math logic can significantly improve performance on large numbers



# MY CODE
def find_gpf(number, current_prime):
    while (current_prime <= number / 2):
        
        while (number % current_prime == 0 and current_prime <= number / 2):
            number = number // current_prime 
        
        while (number % current_prime != 0 and current_prime <= number / 2):
            current_prime = current_prime + 1
    
    return number

print(find_gpf(35, 2)) #7
print(find_gpf(60, 2)) #5
print(find_gpf(10, 2)) #5
print(find_gpf(19, 2)) #19
print(find_gpf(87, 2)) #29
print(find_gpf(100, 2)) #5
print(find_gpf(13195, 2)) #29
print(find_gpf(600851475143, 2)) #6857
print(find_gpf(60085147514312414, 2)) #80309



# MY OLD CODE
#finds greatest prime factor of a number but never of itself
def find_largest_prime_factor(number):
    not_found = True
    current_number = number - 1

    while (not_found and current_number > 1):
        
        if (number % current_number == 0):
            temp = current_number - 1

            while (temp > 1):
                if (current_number % temp == 0):
                    break
                else:
                    temp -= 1
            
            if (temp == 1):
                not_found = False
            else:
                current_number -= 1

        else:
            current_number -= 1
    
    return current_number

#print(find_largest_prime_factor(10)) #5
#print(find_largest_prime_factor(19)) #1
#print(find_largest_prime_factor(87)) #29
#print(find_largest_prime_factor(100)) #5
#print(find_largest_prime_factor(13195)) #29
#print(find_largest_prime_factor(600851475143)) 

"""
Divide by smallest prime number. 
If it does not go in, continue to the next smallest prime number
If it does go in, then add the prime number to the list and continue to divide the prime same smallest number by the new biggest factor
If it does not go in, continue to the next smallest prime number
If it does go in, then add the prime number to the list and continue to divide the prime same smallest number by the new biggest factor
Repeat until you have a list of prime numbers and it is not possible to factor it anymore.
Then take the greatest prime number in the list and there is your answer.
"""