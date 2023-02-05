
from starlite import Controller, Template, get


class SPAController(Controller):
    path = "/"

    @get(path=["", "{p:path}"], include_in_schema=False) 
    def index(self) -> Template:
        return Template(name="app.html.jinja", context={"title": "WEBSEC APP"})
