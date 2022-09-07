import types

import lxml.builder


class ElementMaker(lxml.builder.ElementMaker):
    """
    An lxml ElementMaker with enhancements. As with lxml ElementMaker, "nodes" can be
    strings, dicts, or Elements.

    The following enhancements:

    - Nodes can also be lists / tuples / generators, in which case they are unpacked
      (flattened) into the element. (This is primarily useful for allowing XT
      transformer methods that take a single element to return a list.)
    - `tail` keyword can be defined in the element definition (saves a lot of trouble).
    - Attributes must be given as a mapping (dict, etc.) in children (= args), not as
      **kwargs - provide just one right way to add attributes to elements.
    """

    def __call__(self, tag, *nodes, tail=None):
        def gen_nodes(nodes):
            for node in nodes:
                if isinstance(node, (types.GeneratorType, list, tuple)):
                    for elem in gen_nodes(node):
                        yield elem
                elif node is not None:
                    yield node

        element = lxml.builder.ElementMaker.__call__(self, tag, *gen_nodes(nodes))
        element.tail = tail

        return element
