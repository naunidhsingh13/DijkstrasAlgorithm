from Graph import AdjacencyWeightedGraph as WeightedGraph
from UnionSet import UnionSet


def kruskalMSP(graph):

    union_set = UnionSet(graph.nodes)
    spanning_weight = 0
    spanning_edges = []
    edge_count = 0
    for u, v in sorted(graph.weights.keys(), key=lambda x: graph.weight(x[0], x[1])):
        if union_set.union(u, v):
            spanning_weight += graph.weight(u, v)
            spanning_edges.append((u, v))
            edge_count += 1
            if edge_count == len(graph.nodes)-1:
                break

    return spanning_weight, spanning_edges


if __name__ == "__main__":

    graph = WeightedGraph()
    edges = []
    prev = "AA"
    cnt = 0
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for nch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            edges.append([prev, ch+nch, 4])
            prev = ch+nch
            cnt += 4

    print(cnt)
    edges.pop(0)
    edges.append([prev, "AA", 6])
    graph.load(edges)
    #
    # graph.load([["A", "B", 7],
    #             ["A", "D", 5],
    #             ["B", "C", 8],
    #             ["B", "D", 9],
    #             ["B", "E", 7],
    #             ["C", "E", 5],
    #             ["D", "E", 15],
    #             ["D", "F", 6],
    #             ["E", "F", 8],
    #             ["E", "G", 9],
    #             ["F", "G", 11],
    #             ])

    msp_weight, msp_edges = kruskalMSP(graph)

    print(msp_weight)
    print(", ".join([str(edge) for edge in msp_edges]))
