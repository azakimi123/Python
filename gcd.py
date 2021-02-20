# The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers.

# 1. Compute the remainder of dividing the larger number by the smaller number.
# 2. Replace the larger number with the smaller number and the smaller number with the remainder.
# 3. Repeat this process until the smaller number is zero.

import math

smaller_number = int(input("Enter Smaller Number: "))
larger_number = int(input("Enter Larger Number: "))

def gcd(sm, lg):

  while sm > 0: 
    larger_number = lg
    smaller_number = sm
    sm = larger_number % smaller_number
    larger_number = smaller_number

  print("The Largest Common Divisor is ", larger_number)

gcd(smaller_number,larger_number)

# print(smaller_number)
# print(larger_number)
