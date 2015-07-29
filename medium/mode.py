def SimpleMode(arr):
  from itertools import groupby
  arr = sorted(arr)
  mode = -1, 1
  for k, g in groupby(arr, lambda x: x):
      lg = len(list(g))
      if lg > mode[1]:
          mode = k, lg

  return mode[0]


assert SimpleMode([1, 2, 3, 4, 2 , 4, 5]) == 2




