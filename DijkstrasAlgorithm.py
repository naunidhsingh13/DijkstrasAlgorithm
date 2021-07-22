from Graph import LinkedWeightedGraph
import heapq
from math import inf as infinity
from collections import defaultdict


def get_path(node_label, path_parent_dict):
    path = []
    while node_label is not None:
        path.append(node_label)
        if node_label not in path_parent_dict:
            return []
        node_label = path_parent_dict[node_label]
    return list(reversed(path))


def shortestPath(graph: LinkedWeightedGraph, source: str, destination: str):

    priorityQ = []

    if source not in graph.nodes or destination not in graph.nodes:
        return infinity

    source_node = graph.nodes[source]

    heapq.heappush(priorityQ, (0, source))

    path_parents = {source: None} # change to defaultdict
    distance_map = defaultdict(lambda: infinity)
    distance_map[source_node] = 0

    while priorityQ:

        distance, node_label = heapq.heappop(priorityQ)
        node = graph.nodes[node_label]
        if node.label == destination:
            return distance, get_path(node.label, path_parents)

        for neigh in node.neighs:
            if distance + node.neighs[neigh] < distance_map[neigh]:
                distance_map[neigh] = distance + node.neighs[neigh]
                heapq.heappush(priorityQ, (distance_map[neigh], neigh.label))
                path_parents[neigh.label] = node.label

    return infinity, []


graph = LinkedWeightedGraph()

graph.load([["A", "B", 7],
            ["A", "D", 5],
            ["B", "C", 8],
            ["B", "D", 9],
            ["B", "E", 7],
            ["C", "E", 5],
            ["D", "E", 15],
            ["D", "F", 6],
            ["E", "F", 8],
            ["E", "G", 8],
            ["F", "G", 11],
            ])

dist, path = shortestPath(graph, "A", "G")

print(dist)
print(path)