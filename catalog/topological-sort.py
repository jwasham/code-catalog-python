

def topological_sort(self):
    """
    Determines the priority of vertices to be visited.
    """
    STATUS_STARTED = 1
    STATUS_FINISHED = 2
    order = []
    statuses = {}

    assert (not self.contains_cycle())

    for vertex in self.get_vertex():
        to_visit = [vertex]

        while to_visit:
            v = to_visit.pop()

            if v in statuses:
                if statuses[v] == STATUS_STARTED:
                    statuses[v] = STATUS_FINISHED
                    order.append(v)
            else:
                statuses[v] = STATUS_STARTED
                to_visit.append(v)  # add to stack again to signal vertex has finished DFS

            for u in self.get_neighbor(v):
                if u not in statuses:
                    to_visit.append(u)

    order.reverse()

    return order
