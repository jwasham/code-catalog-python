def parenthesize(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')  # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '  # determine proper separator
            print(sep, end='')
            first_time = False  # any future passes will not be the first
            parenthesize(T, c)  # recur on child
        print(')', end='')  # include closing parenthesis
