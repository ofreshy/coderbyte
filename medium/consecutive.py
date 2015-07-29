def Consecutive(arr):
    sorted_arr = sorted(arr)
    to_add = 0
    for i in range(len(arr) - 1):
        to_add += sorted_arr[i+1] - sorted_arr[i] - 1
    return to_add

assert Consecutive([4, 8, 6]) == 2
assert Consecutive([-2,10,4]) == 10
