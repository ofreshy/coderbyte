def ArithGeo(arr):
  diff = arr[1] - arr[0]
  mult = arr[1] / arr[0]
  for i in range(2, len(arr)):
      if arr[i] - arr[i-1] != diff:
          diff = None
      if arr[i] / arr[i-1] != mult:
          mult = None
      if diff == None and mult == None:
          return -1

  return 'Arithmetic' if diff != None else 'Geometric'

assert ArithGeo([5, 10, 15]) == 'Arithmetic'
assert ArithGeo([2, 4, 8]) == 'Geometric'

