"""
Have the function AdditivePersistence(num)
take the num parameter being passed which will always be a positive integer and
return its additive persistence which is
the number of times you must add the digits in num until you reach a single digit.
For example:
if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.
"""
def AdditivePersistence(num):
  def count(num_str):
    if len(num_str) == 1:
      return 0
    else:
      return count(str(sum([int(s) for s in num_str]))) + 1

  return count(str(num))