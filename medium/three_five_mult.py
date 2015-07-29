def ThreeFiveMultiples(num):
  return sum([n for n in range(3, num) if (n % 3 == 0 or n % 5 == 0)])

print ThreeFiveMultiples(16)
