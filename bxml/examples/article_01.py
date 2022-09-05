"""
An example of a simple XT template.
"""
from copy import deepcopy

from bl.dict import OrderedDict
from bxml.builder import Builder
from bxml.xt import XT

NS = OrderedDict(
    [
        # XML
        ("xml", "http://www.w3.org/XML/1998/namespace"),
        ("xsi", "http://www.w3.org/2001/XMLSchema-instance"),
        # XHTML
        ("html", "http://www.w3.org/1999/xhtml"),
        # Publishing XML
        ("pub", "http://publishingxml.org/ns"),
    ]
)

H = Builder.single(NS.html)
PUB = Builder(default=NS.html, **NS).pub
xt = XT(namespaces=NS)


@xt.register(test="pub:document")
def document(element, **params):
    return PUB.document(
        "\n",
        H.body(
            "\n",
            *xt.transform_all(
                xt.xpath(
                    element,
                    "//html:section[descendant::html:p[contains(@class, 'Article')]]",
                ),
                **params,
            ),
            tail="\n",
        ),
    )


@xt.register(test="html:section[descendant::html:p[contains(@class, 'Article')]]")
def article(element, **params):
    title = "".join(
        xt.xpath(element, "html:p[contains(@class, 'Article-title')]//text()")
    )
    theme = "".join(
        xt.xpath(element, "html:p[contains(@class, 'Article-theme')]//text()")
    )
    if theme:
        title += f" (theme: {theme})"

    return H.section(
        "\n",
        {"class": "Article", "aria-label": title},
        # the following works because element is an iterator of its children
        *xt.transform_all(element, **params),
        tail="\n\n",
    )


# Register the default last so it will be called after all other templates are tried.
@xt.register(test=lambda element, **params: True)
def default(element, **params):
    return deepcopy(element)
