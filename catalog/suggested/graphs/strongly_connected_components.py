def strongly_connected_components(self):
    """
    Compute the vertices in the strongly connected components
    :return list of lists, one for each component's vertices:
    """
    stack = self.scc_dfs_forward_pass()
    components = self.scc_dfs_reverse_pass(stack)

    return components


def scc_dfs_forward_pass(self):
    stack = []
    visited = set()

    for v in self.get_vertex():
        self.dfs_forward(v, stack, visited)

    return stack


def dfs_forward(self, vertex, stack, visited):
    if vertex not in visited:
        visited.add(vertex)
        for u in self.get_neighbor(vertex):
            self.dfs_forward(u, stack, visited)
        stack.append(vertex)


def scc_dfs_reverse_pass(self, stack):
    components = []
    visited = set()

    while stack:
        v = stack.pop()
        if v not in visited:
            component = []
            self.dfs_reverse(v, component, visited)
            component.reverse()
            components.append(component)

    return components


def dfs_reverse(self, vertex, component, visited):
    if vertex not in visited:
        visited.add(vertex)
        component.append(vertex)
        for u in self.get_reverse_neighbor(vertex):
            self.dfs_reverse(u, component, visited)
