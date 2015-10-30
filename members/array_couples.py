"""
Using the Python language,
have the function ArrayCouples(arr) take the arr parameter being passed which will be an array of an even number of positive integers,
and determine if each pair of integers, [k, k+1], [k+2, k+3], etc.
in the array has a corresponding reversed pair somewhere else in the array.

For example: if arr is [4, 5, 1, 4, 5, 4, 4, 1]
then your program should output the string yes because the first pair 4, 5 has the reversed pair 5, 4 in the array,
and the next pair, 1, 4 has the reversed pair 4, 1 in the array as well.
But if the array doesn't contain all pairs with their reversed pairs,
 then your program should output a string of the integer pairs that are incorrect, in the order that they appear in the array.
For example: if arr is [6, 2, 2, 6, 5, 14, 14, 1] then your program should output the string 5,14,14,1 with only a comma separating the integers.
"""

from itertools import chain


def ArrayCouples(couples):
    # keep as list, as we do care about insertion order
    mismatched = []
    for x, y in zip(couples[0::2], couples[1::2]):
        if (y, x) in mismatched:
            mismatched.remove((y, x))
        else:
            mismatched.append((x, y))

    if not mismatched:
        return "yes"

    return ",".join(map(str, chain(*mismatched)))




