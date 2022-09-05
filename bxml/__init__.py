from __future__ import print_function

import os

from bl.dict import Dict
from lxml import etree

from .xml import XML

NS = Dict(
    **{
        "bl": "http://blackearth.us/xml",
    }
)

PATH = os.path.dirname(os.path.abspath(__file__))
JARS = os.path.join(PATH, "jars")
