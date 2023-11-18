from collections import deque
from graph import Graph

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_distances(self, start_node):
        distances = [-1] * (self.graph.num_nodes + 1)
        queue = deque([start_node])
        distances[start_node] = 0

        while queue:
            node = queue.popleft()
            for neighbor in self.graph.edges[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 6
                    queue.append(neighbor)

        return distances[1:]

if __name__ == "__main__":
    n = 5
    edges = [(1, 2), (1, 3), (3, 4)]
    graph = Graph(n)

    for u, v in edges:
        graph.add_edge(u, v)

    bfs = BFS(graph)
    distances = bfs.find_shortest_distances(1)
    print(distances)
