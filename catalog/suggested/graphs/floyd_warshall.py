"""
Graph here:
http://codingjunkie.blogspot.com/2012/10/all-pair-shortest-path-floyd-warshall.html
"""

from pprint import pprint

INF = float('Inf')


def floyd_warshall(graph):
    nodes = graph.keys()

    """ distance[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """

    distance = {}

    for n in nodes:
        distance[n] = {}

        for k in nodes:
            distance[n][k] = graph[n][k]

    """ Add all vertices one by one to the set of intermediate
     vertices.

         ---> Before start of a iteration, we have shortest distances
         between all pairs of vertices such that the shortest
         distances consider only the vertices in set
         {0, 1, 2, .. k-1} as intermediate vertices.

          ----> After the end of a iteration, vertex no. k is
         added to the set of intermediate vertices and the
         set becomes {0, 1, 2, .. k}
    """
    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


if __name__ == '__main__':
    graph = {'A': {'A': 0, 'B': 6, 'C': INF, 'D': 6, 'E': 7},
             'B': {'A': INF, 'B': 0, 'C': 5, 'D': INF, 'E': INF},
             'C': {'A': INF, 'B': INF, 'C': 0, 'D': 9, 'E': 3},
             'D': {'A': INF, 'B': INF, 'C': 9, 'D': 0, 'E': 7},
             'E': {'A': INF, 'B': 4, 'C': INF, 'D': INF, 'E': 0}
             }

    distances = floyd_warshall(graph)

    pprint(distances)
