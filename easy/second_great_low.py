__author__ = 'osharabi'

def SecondGreatLow(arr):
  arr = sorted(set(arr))
  smin, smax = arr[-1], arr[0]
  if len(arr) > 2:
      smin, smax = arr[1], arr[-2]
  return "%s %s" % (smin, smax)




print SecondGreatLow([1, 42, 42, 180])
print SecondGreatLow([90, 23])
print SecondGreatLow([2,2,2,5,5,5,6])