# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)


print(search.breadth_first_graph_search(ab).path())
# Depth
print(search.depth_first_graph_search(ab).path())
#Branch and bound
print(search.ramificacion_acota(ab).path())
#Branch and bound with heuristic
print(search.H_ramificacion_acota(ab).path())



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
