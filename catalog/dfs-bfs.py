

def dfs(self):
    """
    Computes the initial source vertices for each connected component
    and the parents for each vertex as determined through depth-first-search
    :return: initial source vertices for each connected component, parents for each vertex
    :rtype: set, dict
    """
    parents = {}
    components = set()
    to_visit = []

    for vertex in self.get_vertex():
        if vertex not in parents:
            components.add(vertex)
        else:
            continue

        to_visit.append(vertex)

        while to_visit:
            v = to_visit.pop()

            for neighbor in self.get_neighbor(v):
                if neighbor not in parents:
                    parents[neighbor] = v
                    to_visit.append(neighbor)

    return components, parents


def bfs(self):
    """
    Computes the the parents for each vertex as determined through breadth-first search
    :return: parents for each vertex
    :rtype: dict
    """
    parents = {}
    to_visit = queue.Queue()

    for vertex in self.get_vertex():
        to_visit.put(vertex)

        while not to_visit.empty():
            v = to_visit.get()

            for neighbor in self.get_neighbor(v):
                if neighbor not in parents:
                    parents[neighbor] = v
                    to_visit.put(neighbor)

    return parents
