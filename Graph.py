
# Implementations of Graph

class GraphNode:
    def __init__(self, label=None):
        self.label = label
        self.neighs = dict()


class LinkedWeightedGraph:
    """
    - Maintained using GraphNode Class Objects as Vertices keeping pointers to neighbors.
    - Undirected
    - Edges have weights
    """
    def __init__(self):
        self.nodes = dict()

    def load(self, nodes: list[list]):
        for u, v, w in nodes:
            if u not in self.nodes:
                self.nodes[u] = GraphNode(u)
            if v not in self.nodes:
                self.nodes[v] = GraphNode(v)

            self.nodes[u].neighs[self.nodes[v]] = w
            self.nodes[v].neighs[self.nodes[u]] = w


class AdjacencyWeightedGraph:
    # Maintained using Adjacency list
    # Edges have weights
    # vertices can be str or int
    # Undirected
    def __init__(self):
        self.weights = dict()
        self.nodes = set()

    def load(self, nodes: list[list]):
        """
        :param nodes: List[ [ u, v, weight ] ]
        :return:
        """
        for u, v, w in nodes:
            if u > v:
                u, v = v, u
            self.weights[(u, v)] = w
            self.nodes.add(u)
            self.nodes.add(v)

    def weight(self, u, v):

        if u > v:
            u, v = v, u

        if (u, v) in self.weights:
            return self.weights[(u, v)]

        else:
            return None
