# Project Euler: Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below the provided parameter
# value number.


def multipleOf3and5(limit):
    result = 0
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    return result


lim = int(input("Enter Limit to get sum of multiple of 3 and 5 : "))
print(multipleOf3and5(lim))


