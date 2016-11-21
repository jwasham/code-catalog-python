"""Tests if a string of nested braces, parentheses, and brackets are all
matched and nested correctly.
"""


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?
