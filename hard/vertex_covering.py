"""

Using the Python language,
 have the function VertexCovering(strArr) take strArr which will be an array of length three.
  The first part of the array will be a list of vertices in a graph in the form (A,B,C,...),
   the second part of the array will be the edges connecting the vertices in the form
(A-B,C-D,...) where each edge is bidirectional.
 The last part of the array will be a set of vertices in the form (X,Y,Z,...) a
 nd your program will have to determine whether or not the set of vertices given covers every edge in the graph
 such that every edge is incident to at least one vertex in the set.
  For example: if strArr is ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(A,B)"]
   then the vertices (A,B) are in fact one of the endpoints of every edge in the graph,
   so every edge has been accounted for. Therefore your program should return the string yes.
    But, if for example the last part of the array was (C,B) then these vertices don't cover all the edges because
    the edge connecting A-D is left out. If this is the case your program should return the edges given in the
    second part of the array that are left out in the same order they were listed, so for this example your
     program should return (A-D).

The graph will have at least 2 vertices and all the vertices in the graph will be connected. The third part of the array listing the vertices may be empty, where it would only contain the parenthesis with no values within it: "()"
"""

def VertexCovering(strArr):
  heads, edges, points = [s.replace('(', '').replace(')', '') for s in strArr]
  edge_list = edges.split(',')
  unaccounted_for = set(edge_list)

  for edge in edge_list:
      for p in points.split(','):
          if p and p in edge and edge in unaccounted_for:
              unaccounted_for.remove(edge)
      if not unaccounted_for:
          break

  if unaccounted_for:
      return '(' + ','.join([e for e in edge_list if e in unaccounted_for]) + ')'
  else:
      return 'yes'


assert VertexCovering(["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C)"]) == '(A-B,A-D,B-D)'
assert VertexCovering(["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z)","(Z,Y,Q)"]) == 'yes'
assert VertexCovering(["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(A,B)"]) == 'yes'
print VertexCovering(["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z,X-Q)","()"])


