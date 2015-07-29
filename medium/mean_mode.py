def MeanMode(arr):
  arr = sorted(arr)
  n = len(arr)
  the_mean = sum(arr) / (n * 1.0)
  if n % 2 == 0:
      the_mode = (arr[n/2] + arr[n/2 - 1]) / 2.0
  else:
      the_mode = arr[n/2]

  return int(the_mean == the_mode)


print MeanMode([1,2,3,4])
