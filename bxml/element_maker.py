import lxml.builder
import types


class ElementMaker(lxml.builder.ElementMaker):
    """
    An ElementMaker with the following enhancements:

    - `tail` can be defined right in the element definition (saves a lot of trouble).
    - Attributes must be given as a mapping (dict, etc.) in children (= args), not as
      **kwargs - provide just one right way to add attributes to elements.
    - [DISABLED] unpack nested lists of children into a single list.
    """

    def __call__(self, tag, *elements, tail=None):
        def gen_elements(elements):
            for element in elements:
                if isinstance(element, (types.GeneratorType, list, tuple)):
                    for elem in gen_elements(element):
                        yield elem
                else:
                    yield element

        e = lxml.builder.ElementMaker.__call__(self, tag, *gen_elements(elements))
        e.tail = tail
        return e
