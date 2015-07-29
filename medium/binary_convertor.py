def BinaryConverter(str):
  sum = 0
  n = len(str) - 1
  for i, d in enumerate(str):
      sum += (2 **  (n-i)) * int(d)
  return '%s' % sum


assert BinaryConverter('100101') == '37'
assert BinaryConverter('011') == '3'