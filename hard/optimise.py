
a = range(1, 4)
import itertools
b = itertools.permutations(a)
mat = [(1,2,1), (4,1,5) , (5,2,1)]





lowest_cost = None
best_perm = None
for perm in b:
    total_cost = mat[0][perm[0]-1] + mat[1][perm[1]-1] + mat[2][perm[2]-1]
    if lowest_cost is None or lowest_cost > total_cost:
        lowest_cost = total_cost
        best_perm = perm

print best_perm
print '----'


def OptimalAssignments(strArr):
    mat = [eval(l) for l in strArr]
    r = range(0, len(mat))

    import itertools
    perms = itertools.permutations(r)

    lowest_cost = -1
    for perm in perms:
        cost = sum([mat[i][perm[i]] for i in r])
        if lowest_cost < 0 or cost < lowest_cost:
            lowest_cost = cost
            best_perm = perm
    print best_perm
    return ''.join(['(%s-%s)' % (i+1, best_perm[i]+1) for i in r])





print OptimalAssignments(["(13,4,7,6)","(1,11,5,4)","(6,7,2,8)","(1,3,5,9)"])



