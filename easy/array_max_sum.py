def ArrayAdditionI(arr):
  from itertools import combinations
  sorted_arr = sorted(arr)
  max_element = sorted_arr[-1]
  rest_arr = sorted_arr[:-1]
  for i in range(2, len(sorted_arr)):
      for comb in combinations(rest_arr, i):
          if sum(comb) == max_element:
              return 'true'
  return 'false'


print ArrayAdditionI([10,20,30,40,100])
print ArrayAdditionI([3,5,-1,0,13])
print ArrayAdditionI([5,7,16,1,2])