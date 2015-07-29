"""
have the function FarthestNodes(strArr) read strArr which will be an array of hyphenated letters representing paths between those two nodes.
For example: ["a-b","b-c","b-d"] means that there is a path from node a to b (and b to a), b to c, and b to d.
 Your program should determine the longest path that exists in the graph and return the length of that path.
 So for the example above,
 your program should return 2 because of the paths a-b-c and d-b-c.
 The path a-b-c also means that there is a path c-b-a.
 No cycles will exist in the graph and every node will be connected to some other node in the graph.

Hard challenges are worth 15 points and you are not timed for them. Use the Parameter Testing feature in the box below to test your code with different arguments.
"""


def FarthestNodes(strArr):
    tree = as_tree(strArr)
    paths = [farthest(tree, [t]) for t in tree.keys()]
    return len(max(paths, key=len)) - 1



def as_tree(connections):
    from collections import defaultdict
    def default_factory():
        return []

    tree = defaultdict(default_factory)
    for connection in connections:
        n1, n2 = connection.split('-')
        tree[n1].append(n2)
        tree[n2].append(n1)

    return tree


def farthest(tree, paths):
    new_paths = []
    for path in paths:
        last_node = path[-1]
        children = tree[last_node]
        for child in children:
            if child not in path:
                new_paths.append(path + child)
    if not new_paths:
        return max(paths, key=len)
    return farthest(tree, new_paths)











print FarthestNodes(["a-b","b-c","b-d"]) == 2
print FarthestNodes(["b-e","b-c","c-d","a-b","e-f"]) == 4
print FarthestNodes(["b-a","c-e","b-c","d-c" ]) == 3
