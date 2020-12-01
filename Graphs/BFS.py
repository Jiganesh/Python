import collections
d = {

    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["F", "G"]

}


def bfs(graph, root):

    visited, queue = [], collections.deque([root])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


print(bfs(d, "A"))


'''
Time Compexity O(V+E)
Space Complexity O(V)


To build Index by Search Index
For GPS Navigation
Path Finding Algorithm
Cycle Detection in Undirected Graph
'''
