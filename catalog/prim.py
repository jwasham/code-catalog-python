import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted:
    def get_vertex():
        """Just a placeholder"""
        pass

    def get_neighbor(vertex):
        """Just a placeholder"""
        pass

    def prim(self):
        """
        Returns a dictionary of parents of vertices in a minimum spanning tree
        :rtype: dict
        """
        s = set()
        q = queue.PriorityQueue()
        parents = {}
        start_weight = float("inf")
        weights = {}  # since we can't peek into queue

        for i in self.get_vertex():
            weight = start_weight
            if i == 0:
                q.put(([0, i]))
            weights[i] = weight
            parents[i] = None

        while not q.empty():
            v_tuple = q.get()
            vertex = v_tuple[1]

            s.add(vertex)

            for u in self.get_neighbor(vertex):
                if u.vertex not in s:
                    if u.weight < weights[u.vertex]:
                        parents[u.vertex] = vertex
                        weights[u.vertex] = u.weight
                        q.put(([u.weight, u.vertex]))

        return parents


def main():
    g = GraphUndirectedWeighted(9)
    g.add_edge(0, 1, 4)
    ...

    msp = g.prim()
    print(msp)
    # parents of each vertex
    assert (msp == {0: None, 1: 0, 2: 1, 3: 2, 4: 5, 5: 3, 6: 5, 7: 3, 8: 6})


if __name__ == "__main__":
    main()
