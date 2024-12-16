from __future__ import annotations
from typing import TYPE_CHECKING
from round_of_actions_factory import parse_list_to_rounds_of_actions
from file_io import parse_txt_to_list

if TYPE_CHECKING:
    from view import View
    from model import Model


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.input_path = None
        self.all_rounds = []
        self.view = view
        self.model = model
        self.init_view_buttons()

    def init_view_buttons(self) -> None:
        self.view.path_button_on_click(self.get_input_path)
        self.view.read_button_on_click(self.process_input_file)

    def get_input_path(self, event) -> None:
        self.input_path = self.view.open_txt_file()
        return "break"

    def parse_input_file(self) -> None:
        txt_list = parse_txt_to_list(path=self.input_path)
        return parse_list_to_rounds_of_actions(txt_list=txt_list)

    def process_input_file(self, event) -> None:
        (
            self.all_rounds,
            total_actions,
            total_known_actions,
            total_unknown_actions,
            unknown_lines,
        ) = self.parse_input_file()
        self.print_to_view(
            self.create_summary(
                total_actions, total_known_actions, total_unknown_actions
            )
        )
        return "break"

    def create_summary(
        self, total_actions: str, total_known_actions: str, total_unknown_actions: str
    ) -> str:
        return "--------------------\nTotal Actions: {}\nKnown_actions: {}\nUnknown Actions: {}\n--------------------\n".format(
            total_actions, total_known_actions, total_unknown_actions
        )

    def print_to_view(self, content) -> None:
        self.view.text_field.insert("end", content)
        self.view.text_field.see("end")

    def run(self) -> None:
        self.view.mainloop()
