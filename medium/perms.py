def PermutationStep(num):
  from itertools import permutations
  m = num
  minum = -1
  for perm in permutations(str(num), len(str(num))):
    n = int(''.join(perm))
    if n > num and n-num < m:
      m = n - num
      minum = n
  return minum

print PermutationStep(123)