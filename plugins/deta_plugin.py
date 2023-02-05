from typing import Any
from starlite import PluginProtocol, Provide, Starlite
from aiodeta import Deta as AioDeta
from deta import Deta
import os


class ODetaMPlugin(PluginProtocol[Any]):
    _aiodeta: AioDeta
    _deta: Deta

    def __init__(self) -> None:

        super().__init__()
        self._aiodeta = AioDeta(os.getenv('PROJECT_KEY'))
        self._deta = Deta(os.getenv('PROJECT_KEY'))

    def get_aiodeta(self) -> AioDeta:
        return self._aiodeta

    def get_deta(self) -> Deta:
        return self._deta

    def on_app_init(self, app: Starlite) -> None:
        app.dependencies.update(
            {"aiodeta": Provide(self.get_aiodeta), "deta": Provide(self.get_deta)})
        return super().on_app_init(app)
