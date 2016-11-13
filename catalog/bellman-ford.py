"""
The Bellman-Ford algorithm
Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbors of u
    graph[u][v] gives weight of edge (u, v)
"""


# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {}  # Stands for destination
    p = {}  # Stands for predecessor
    for node in graph:
        d[node] = float('Inf')  # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0  # For the source we know how to reach
    return d, p


def relax(node, neighbor, graph, d, p):
    # If the distance between the node and the neighbor is lower than the one I have now
    if d[neighbor] > d[node] + graph[node][neighbor]:
        # Record this lower distance
        d[neighbor] = d[node] + graph[node][neighbor]
        p[neighbor] = node


def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph) - 1):  # Run this until is converges
        for u in graph:
            for v in graph[u]:  # For each neighbor of u
                relax(u, v, graph, d, p)  # Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p


def test():
    graph = {
        'a': {'b': -1, 'c': 4},
        'b': {'c': 3, 'd': 2, 'e': 2},
        'c': {},
        'd': {'b': 1, 'c': 5},
        'e': {'d': -3}
    }

    d, p = bellman_ford(graph, 'a')

    assert d == {
        'a': 0,
        'b': -1,
        'c': 2,
        'd': -2,
        'e': 1
    }

    assert p == {
        'a': None,
        'b': 'a',
        'c': 'b',
        'd': 'e',
        'e': 'b'
    }


if __name__ == '__main__':
    test()
