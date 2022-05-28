import inspect

import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp import page

imports = list(globals().values())

for x in imports:
    if inspect.isclass(x):
        if issubclass(x, page.Page) and x is not page.Page:
            jp.Route(x.path, x.serve)


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
