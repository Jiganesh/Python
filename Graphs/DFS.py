d= {

"A":["B","D"],
"B":["A","C"],
"C":["B"],
"D":["A","E","F"],
"E":["D","F","G"],
"F":["D","E","H"],
"G":["E","H"],
"H":["F","G"]

          }

def dfs(visited, graph, node):
          if node not in visited:
                    visited.append(node)
                    for neighbour in graph[node]:
                              dfs(visited,graph, neighbour)
          return visited

print(dfs([],d,"A"))


'''
Time Complexity O(V+E)
Space Complexity O(V)

For finding the path
To test if the graph is bipartite
For finding the strongly connected components of a graph
For detecting cycles in a graph
'''
