

def contains_cycle(self):
    """
    Determines if one of the connected components contains a cycle
    :return: true if one of the connected components contains a cycle
    :rtype: bool
    """
    contains_cycle = False
    STATUS_STARTED = 1
    STATUS_FINISHED = 2

    for vertex in self.get_vertex():
        statuses = {}
        to_visit = [vertex]

        while to_visit and not contains_cycle:
            v = to_visit.pop()

            if v in statuses:
                if statuses[v] == STATUS_STARTED:
                    statuses[v] = STATUS_FINISHED
            else:
                statuses[v] = STATUS_STARTED
                to_visit.append(v)  # add to stack again to signal vertex has finished DFS

            for u in self.get_neighbor(v):
                if u in statuses:
                    if statuses[u] == STATUS_STARTED:
                        contains_cycle = True
                        break
                else:
                    to_visit.append(u)

            if contains_cycle:
                break

    return contains_cycle
