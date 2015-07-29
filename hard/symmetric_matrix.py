"""
Using the Python language,
 have the function SymmetricMatrix(strArr) read strArr which will be an array of integers represented as strings.
 Within the array there will also be "<>" elements which represent break points.
 The array will make up a matrix where the (number of break points + 1) represents the number of rows.
 Here is an example of how strArr may look: ["1","0","1","<>","0","1","0","<>","1","0","1"].
 There are two "<>", so 2 + 1 = 3.
 Therefore there will be three rows in the array and the contents will be row1=[1 0 1], row2=[0 1 0] and row3=[1 0 1].
 Your program should take the given array of elements,
 create the proper matrix,
 and then determine whether the matrix is symmetric,
 in other words,
 if matrix M is equal to M transpose.
 If it is,
 return the string symmetric and if it isn't return the string not symmetric.
 A matrix may or may not be a square matrix and if this is the case you should return the string not possible.
 For the example above, your program should return symmetric.
"""


def SymmetricMatrix(strArr):
    as_list = [int(e) for e in strArr if e != '<>']
    n = len(strArr) - len(as_list) + 1

    # For a square matrix, the number of elements in the matrix should be n squared
    if n**2 != len(as_list):
        return 'not possible'

    for i in range(0, n-1):
        for j in range(i+1, n):
            if as_list[i * n + j] != as_list[j * n + i]:
                return 'not symmetric'

    return 'symmetric'



assert SymmetricMatrix(["1","0","1","<>","0","1","0","<>","1","0","1"]) == 'symmetric'
assert SymmetricMatrix(["5","0","<>","0","5"]) == 'symmetric'
assert SymmetricMatrix(["1","2","4","<>","2","1","1","<>","-4","1","-1"]) == 'not symmetric'
assert SymmetricMatrix(["1","2","<>","2","1","<>","1","-1"]) == 'not possible'
