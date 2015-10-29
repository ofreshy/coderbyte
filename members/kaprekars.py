"""
Using the Python language,
have the function KaprekarsConstant(num) take the num parameter being passed which will be a 4-digit number with at least two distinct digits.
Your program should perform the following routine on the number:
  Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number),
  and subtract the smaller number from the bigger number.
  Then repeat the previous step.
Performing this routine will always cause you to reach a fixed number: 6174.
 Then performing the routine on 6174 will always give you 6174 (7641 - 1467 = 6174).
 Your program should return the number of times this routine must be performed until 6174 is reached.
 For example:
 if num is 3524 your program should return 3 because of the following steps:
 (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174.
"""

def KaprekarsConstant(num):
    def calc(a_num, num_calc):
        if a_num == 6174:
            return num_calc

        num_str = str(a_num)
        if len(num_str) < 4:
            a_num *= 10**(4-len(num_str))
            num_str = str(a_num)

        max_num = int("".join(sorted(num_str, reverse=True)))
        min_num = int("".join(sorted(num_str)))
        new_num = max_num - min_num
        return calc(new_num, num_calc+1)

    return calc(num, 0)




