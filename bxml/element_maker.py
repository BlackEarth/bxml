import lxml.builder


class ElementMaker(lxml.builder.ElementMaker):
    """
    An ElementMaker with the following enhancements:

    - `tail` can be defined right in the element definition (saves a lot of trouble).
    - Attributes must be given as a mapping (dict, etc.) in children (= args), not as
      **kwargs - provide just one right way to add attributes to elements.
    - [DISABLED] unpack nested lists of children into a single list.
    """

    def __call__(self, tag, *children, tail=None):
        # def list_children(children):
        #     child_list = []
        #     for ch in children:
        #         if isinstance(ch, list):
        #             child_list += list_children(ch)
        #         else:
        #             child_list.append(ch)
        #     return child_list
        def list_children(children):
            return children

        e = lxml.builder.ElementMaker.__call__(self, tag, *list_children(children))
        e.tail = tail
        return e
