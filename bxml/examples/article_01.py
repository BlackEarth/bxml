"""
An example of a simple XT template.
"""
from copy import deepcopy

from bxml import NS
from bxml.builder import Builder
from bxml.xt import XT

H = Builder.single(NS.html)
PUB = Builder.single(NS.pub)
xt = XT(namespaces=NS)


@xt.register(test="pub:document")
def document(element, **params):
    return PUB.document(
        "\n",
        H.body(
            "\n",
            *[
                xt.transform(elem, **params)
                for elem in xt.xpath(
                    element,
                    "//html:section[descendant::html:p[contains(@class, 'Article')]]",
                )
            ],
        ),
        tail="\n",
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
        *[xt.transform(child, **params) for child in element],
        tail="\n\n",
    )


# Register the default last so it will be called after all other templates are tried.
@xt.register(test=lambda element, **params: True)
def default(element, **params):
    return deepcopy(element)
