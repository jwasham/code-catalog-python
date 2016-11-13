import array
from sys import getsizeof, stderr
from itertools import chain
from collections import deque

try:
    from reprlib import repr
except ImportError:
    pass

print("{:<20}{:<15}{:<15}".format("Item", "sys.getsizeof", "recursive total"))


def print_size(name, item):
    print("{:<20}{:<15}{:<15}".format(name, getsizeof(item), total_size(item)))


def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                    }
    all_handlers.update(handlers)  # user handlers take precedence
    seen = set()  # track which object id's have already been seen
    default_size = getsizeof(0)  # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:  # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


print_size("int", 1)
print_size("large int", 4000000000000000)
print_size("super int", 400000000000000000000000000000000)
print_size("float", 1.5)
print_size("high prec float", 87982375982735876398629351.82369872635987263589726358976235)
print_size("string(1)", "h")
print_size("string(5)", "hello")
print_size("string(10)", "helloworld")
print_size("list - empty", [])
print_size("list - 1", [1])
print_size("list - 2", [1, 2])
print_size("list - 3", [1, 2, 35])
print_size("list - 2 large", [18972938987239587239557, 2097230970239523])
print_size("list - 3 large", [18972938987239587239557, 2097230970239523, 18972938987239587239557])
print_size("list - 4 large", [18972938987239587239557, 2097230970239523, 18972938987239587239557, 235])
print_size("list - 1 string", ["again"])
print_size("list - 2 string", ["hello", "again"])
print_size("list - 3 string", ["hello", "again", "there"])

a5 = array.array('b')
print_size("array - 0 b", a5)

a1 = array.array('b')
a1.append(1)
print_size("array - 1 b", a1)

a2 = array.array('b')
for i in range(10):
    a2.append(i)
print_size("array - 10 b", a2)

a3 = array.array('b')
for i in range(128):
    a3.append(i)
print_size("array - 128 b", a3)

a4 = array.array('b', [0] * 256)
print_size("array - 256 b", a4)

print_size("dict - empty", {})
print_size("dict - 1", {"hi": 1})
print_size("dict - 2", {"h": 1, "i": 2})
print_size("dict - 4", {"h": 1, "i": 2, "j": 3, "k": 4})

print_size("set - empty", set())
print_size("set - 1", {1})
print_size("set - 2", {1, 2})
print_size("set - 4", {1, 2, 3, 4})
