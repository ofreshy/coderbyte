__author__ = 'osharabi'

def ArithGeoII(arr):
    if len(arr) <= 1:
        return -1

    diff = arr[1] - arr[0]
    mult = arr[1] / arr[0]
    i = 1
    while (i+1) < len(arr) and not (diff is  None and mult is None):
        cur_diff = arr[i+1] - arr[i]
        curr_mult = arr[i+1] / arr[i]
        if cur_diff != diff:
            diff = None
        if curr_mult != mult:
            mult = None
        i += 1

    if diff != None:
        return 'Arithmetic'
    if mult != None:
        return 'Geometric'
    return -1



assert ArithGeoII([1,2,3,100]) == -1
assert ArithGeoII([-2, -6, -18, -54]) == 'Geometric'
assert ArithGeoII([2, 6, 18, 54]) == 'Geometric'
assert ArithGeoII([5, 10, 15]) == "Arithmetic"
assert ArithGeoII([2, 4, 6]) == "Arithmetic"
assert ArithGeoII([-4, 4, 12]) == "Arithmetic"
