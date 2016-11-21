import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):

    ...

    def dijkstra(self, source, dest):
        q = queue.PriorityQueue()
        parents = []
        distances = []
        start_weight = float("inf")

        for i in self.get_vertex():
            weight = start_weight
            if source == i:
                weight = 0
            distances.append(weight)
            parents.append(None)

        q.put(([0, source]))

        while not q.empty():
            v_tuple = q.get()
            v = v_tuple[1]

            for e in self.get_neighbor(v):
                candidate_distance = distances[v] + e.weight
                if distances[e.vertex] > candidate_distance:
                    distances[e.vertex] = candidate_distance
                    parents[e.vertex] = v
                    # primitive but effective negative cycle detection
                    if candidate_distance < -1000:
                        raise Exception("Negative cycle detected")
                    q.put(([distances[e.vertex], e.vertex]))

        shortest_path = []
        end = dest
        while end is not None:
            shortest_path.append(end)
            end = parents[end]

        shortest_path.reverse()

        return shortest_path, distances[dest]


def main():
    g = GraphUndirectedWeighted(9)
    g.add_edge(0, 1, 4)
    ...

    shortest_path, distance = g.dijkstra(0, 1)
    assert shortest_path == [0, 1] and distance == 4


if __name__ == "__main__":
    main()
