"""
Using the Python language,
 have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph.
  The structure of the array will be as follows: The first element in the array will be the number of nodes N (points)
  in the array as a string.
  The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.).
  Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes.
   They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.).
   Although, there may exist no connections at all.

An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. It may help to visualize the Graph by drawing out the nodes and their connections. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.
"""

def ShortestPath(strArr):
    N = int(strArr[0])
    nodes = strArr[1:N+1]
    connections = [f.split('-') for f in strArr[N+1:]]

    as_tree = {n: set() for n in nodes}
    for f, t in connections:
        as_tree[f].add(t)
        as_tree[t].add(f)

    start_node = nodes[0]
    goal_node = nodes[-1]

    def get_to_goal(visited_nodes, paths):
        if not paths:
            return None

        new_paths = []
        for path in paths:
            last = path[-1]
            children = as_tree[last]
            for child in children:
                if child not in visited_nodes:
                    visited_nodes.add(child)
                    new_path = path + [child]
                    if child == goal_node:
                        return new_path
                    new_paths.append(new_path)
        return get_to_goal(visited_nodes, new_paths)

    shortest_path = get_to_goal({start_node}, [[start_node]])
    return "-".join(shortest_path) if shortest_path else -1



assert ShortestPath(["4","A","B","C","D","A-B","B-D","B-C","C-D"]) == "A-B-D"
assert ShortestPath([ "5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]) == "A-C-D-F"
assert ShortestPath([ "4","X","Y","Z","W","X-Y","Y-Z","X-W"]) == "X-W"
assert ShortestPath([ "4","X","Y","Z","W"]) == -1