def FibonacciChecker(num):
  cur = (1, 2)
  if num in cur:
    return 'yes'

  while num >= cur[1]:
      cur = cur[0], sum(cur)
      if num == cur[1]:
          return 'yes'
  return 'no'


print FibonacciChecker(34)