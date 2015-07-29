"""
Using the Python language, have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number, otherwise return 0. For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019, both of which are primes.

Use the Parameter Testing feature in the box below to test your code with different arguments.
"""

from itertools import permutations

def is_prime(num):
    if num == 1:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    for i in xrange(1, int(num/2)):
        if num % ((i*2) + 1) == 0:
            return False
    return True


def PrimeChecker(num):
    # perm will return 11 , 11 for 11, so only iterate over unique values
    for perm in set(permutations(str(num))):
        if is_prime(int(''.join(perm))):
            return 1
    return 0

print PrimeChecker(100)
