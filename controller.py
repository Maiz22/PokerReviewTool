from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from view import View
    from model import Model

class Controller:
    def __init__(self, view:View, model:Model) -> None:
        self.view = view
        self.model = model

    def run(self) -> None:
        self.view.mainloop()