"""
have the function MaxHeapChecker(arr) take arr which represents a heap data structure
and determine whether or not it is a max heap.
A max heap has the property that all nodes in the heap are either greater than or equal to each of its children.
For example:
if arr is [100,19,36,17] then this is a max heap and your program should return the string max.
If the input is not a max heap then your program should return a list of nodes in string format,
in the order that they appear in the tree,
that currently do not satisfy the max heap property because the child nodes are larger than their parent.
For example: if arr is [10,19,52,13,16] then your program should return 19,52.
"""


def MaxHeapChecker(arr):
    bad_boys = []
    for idx in range(1, len(arr)):
        parent = arr[(idx-1)/2]
        child = arr[idx]
        if child > parent:
            bad_boys.append(str(child))

    return ','.join(bad_boys) if bad_boys else 'max'
