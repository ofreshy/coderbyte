"""
Using the Python language,
have the function ArrayAddition(arr) take the array of numbers stored in arr and return the string true
if any combination of numbers in the array can be added up to equal the largest number in the array,
otherwise return the string false.
For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23.
 The array will not be empty, will not contain all the same elements, and may contain negative numbers.


"""
import itertools
def ArrayAddition(arr):
  arr = sorted(arr)

  for n in range(2, len(arr)):
    for lst in itertools.combinations(arr, n):
      if sum(lst) == arr[-1]:
        return "true"
  return "false"


# assert ArrayAddition([0, 4, 1, 2]) == 'true'
# assert ArrayAddition([5,7,16,1,2]) == 'false'
# assert ArrayAddition([-1, 7, 9, 3]) == 'true'
# assert ArrayAddition([10,12,500,1,-5,1,0]) == 'true'


def OffLineMinimum(strArr):
    cur_set = set()
    answer = []
    for l in strArr:
        if l == 'E':
            min_num = min(cur_set)
            answer.append(str(min_num))
            cur_set.remove(min_num)
        else:
          cur_set.add(int(l))
    return ','.join(answer)

print OffLineMinimum(["1","2","E","E","3"])
print OffLineMinimum(["5","4","6","E","1","7","E","E","3","2"] )