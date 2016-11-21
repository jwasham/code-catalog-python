from copy import deepcopy


def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)  # imported from copy module
    verts = list(closure.vertices())  # make indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that edge (i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # verify that edge (k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i,j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure


if __name__ == '__main__':
    from graph_examples import figure_14_11 as example

    g = example()
    print("Number of vertices is", g.vertex_count())
    print("Number of edges is", g.edge_count())
    closure = floyd_warshall(g)
    print("Number of edges in closure is", closure.edge_count())
