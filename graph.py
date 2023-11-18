class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = {i: [] for i in range(1, num_nodes + 1)}

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
