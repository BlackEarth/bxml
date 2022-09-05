from __future__ import print_function

import os

from bl.dict import OrderedDict

from .xml import XML

NS = OrderedDict(
    [
        # XML
        ("xml", "http://www.w3.org/XML/1998/namespace"),
        ("xsi", "http://www.w3.org/2001/XMLSchema-instance"),
        # XHTML
        ("html", "http://www.w3.org/1999/xhtml"),
    ]
)

PATH = os.path.dirname(os.path.abspath(__file__))
JARS = os.path.join(PATH, "jars")
