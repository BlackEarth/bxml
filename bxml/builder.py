import logging

from bl.dict import Dict

from .element_maker import ElementMaker
from .xml import XML

log = logging.getLogger(__name__)


class Builder(Dict):
    """
    Create a set of ElementMaker methods all bound to the same object.
    """

    def __init__(self, default=None, **namespaces):
        Dict.__init__(self)
        if default is not None:
            nsmap = {None: default}
            nsmap.update(
                **{
                    k: namespaces[k]
                    for k in namespaces.keys()
                    if namespaces[k] != default
                }
            )
        else:
            nsmap = namespaces
        self.__dict__["nsmap"] = nsmap
        for key in namespaces:  # each namespace gets its own method. named for its key
            self[key] = ElementMaker(namespace=namespaces[key], nsmap=nsmap)
        self._ = ElementMaker(namespace=default, nsmap=nsmap)

    @classmethod
    def single(C, namespace=None):
        """
        Create an ElementMaker with an optional single namespace that uses that
        namespace as the default.
        """
        if namespace is None:
            B = C()._
        else:
            B = C(default=namespace, _=namespace)._

        return B
