

def WeightedPath(str_arr):
    n = int(str_arr[0])
    nodes = str_arr[1:n+1]
    connections = str_arr[n+1:]

    tree = dict()
    for connection in connections:
        f, t, w = connection.split('|')
        if f not in tree:
            tree[f] = []
        if not t in tree:
            tree[t] = []
        tree[f].append((t, int(w)))
        tree[t].append((f, int(w)))
    # quick check
    first = nodes[0]
    if first not in tree:
        return -1
    # longer check
    def find_best_path(tree, paths, best_path, end):
        if not paths:
            return best_path

        new_paths = []

        for path, weight in paths:
            split = path.split('-')
            last = split[len(split)-1]
            if last == end:
                if weight < best_path[1]:
                    best_path = path, weight
                continue

            if not last in tree:
                continue

            vs = tree[last]
            for v in vs:
                if v[0] in split:
                    continue

                new_path = path + '-' + v[0]
                new_weight = weight + v[1]
                if new_weight > best_path[1]:
                   continue

                new_paths.append((new_path, new_weight))

        return find_best_path(tree, new_paths, best_path, end)

    bb = find_best_path(tree, [(first, 0)], (-1, 10000000), nodes[len(nodes)-1])
    if bb[0] == -1:
        return -1
    else:
        return bb[0]







m1 = ["7","A","B","C","D","E","F","G","A|B|1","A|E|9","B|C|2","C|D|1","D|F|2","E|D|6","F|G|2"]
m2 = ["4","A","B","C","D", "A|B|2", "C|B|11", "C|D|3", "B|D|2"]
m3 = ["4","x","y","z","w","x|y|2","y|z|14", "z|y|31"]
m4 = ["6","A","B","C","D","E","F","B|A|2","A|F|12","A|C|4","B|D|1","D|E|1","C|D|4","F|E|1"]
m5 = ["3","GG","HH","JJ","GG|JJ|6","GG|HH|2","JJ|HH|2"]

assert WeightedPath(m1) == 'A-B-C-D-F-G'
assert WeightedPath(m2) == 'A-B-D'
assert WeightedPath(m3) == -1
assert WeightedPath(m4) == 'A-B-D-E-F'
assert WeightedPath(m5) == 'GG-HH-JJ'




