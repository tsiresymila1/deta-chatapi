
from starlite import Router
from app.spa import SPAController
from app.storage import download

web_router = Router(path="/", route_handlers=[download, SPAController])
